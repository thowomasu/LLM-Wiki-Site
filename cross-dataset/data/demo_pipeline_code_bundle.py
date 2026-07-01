"""Public code bundle for the cross-dataset pulse-to-EIS demo.



This file contains the core functions shown in the HTML presentation.

It is a reading and handoff artifact, not a standalone replacement for the repo.

"""

# 1. Demo scoring pipeline.

def demo_score(max_train_rows: int, max_holdout_rows: int) -> dict[str, Any]:
    dev = pd.read_csv(DEV_MATRIX_CSV)
    holdout = pd.read_csv(MOLICELL_MATRIX_CSV)
    targets = target_columns(dev)
    train = dev[dev["split_role"] == "dev_train_seen_outcome"].head(max_train_rows).copy()
    test = holdout[holdout["split_role"] == "molicell_p42a_whole_dataset_holdout_not_tuned"].head(max_holdout_rows).copy()
    if train.empty or test.empty:
        raise RuntimeError("Demo needs non-empty dev train rows and Molicell holdout rows.")
    train = add_derived_features(train)
    test = add_derived_features(test)
    for col in FEATURE_COLUMNS + targets:
        train[col] = pd.to_numeric(train[col], errors="coerce")
        test[col] = pd.to_numeric(test[col], errors="coerce")
    train = train.dropna(subset=targets).copy()
    test = test.dropna(subset=targets).copy()

    train_y = train[targets].to_numpy()
    test_y = test[targets].to_numpy()
    baseline_pred = np.tile(np.nanmean(train_y, axis=0), (len(test), 1))
    model = build_model(KNeighborsRegressor(n_neighbors=3), FEATURE_COLUMNS)
    model.fit(train[FEATURE_COLUMNS], train[targets])
    knn_pred = model.predict(test[FEATURE_COLUMNS])
    model_pred = 0.8 * baseline_pred + 0.2 * knn_pred

    baseline_metrics = metric_payload(test_y, baseline_pred, targets)
    model_metrics = metric_payload(test_y, model_pred, targets)
    improvement = float(
        (baseline_metrics["rmse_all_ohm"] - model_metrics["rmse_all_ohm"])
        / baseline_metrics["rmse_all_ohm"]
    )
    kk_rows, kk_summary = validate_matrix(test, "demo_molicell_subset")
    pairs = target_frequency_pairs(targets)
    input_columns = [
        "sample_id",
        "dataset",
        "split_role",
        "cell_id",
        "soc_percent",
        "temperature_c",
        "td_rows",
        "td_duration_s",
        "td_voltage_start_v",
        "td_voltage_end_v",
        "td_voltage_min_v",
        "td_voltage_max_v",
        "td_voltage_mean_v",
        "td_voltage_std_v",
        "td_current_mean_a",
        "td_current_abs_mean_a",
        "td_current_abs_max_a",
        "td_active_fraction",
        "td_charge_throughput_ah",
        "td_discharge_throughput_ah",
    ]
    results = {
        "experiment": "cross_dataset_pulse_to_eis_training_demo",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "claim_boundary": "Demo only. Uses a bounded subset and does not create a new validation claim.",
        "inputs": {
            "dev_matrix_csv": str(DEV_MATRIX_CSV),
            "molicell_matrix_csv": str(MOLICELL_MATRIX_CSV),
            "train_rows_used": int(len(train)),
            "holdout_rows_used": int(len(test)),
            "feature_columns": FEATURE_COLUMNS,
            "target_columns": targets,
            "frequency_grid_hz": [row["frequency_hz"] for row in pairs],
            "train_preview_rows": records_preview(train, input_columns, rows=3),
            "holdout_preview_rows": records_preview(test, input_columns + targets[:6], rows=3),
        },
        "method": {
            "baseline": "global train target mean",
            "model": "KNeighborsRegressor(n_neighbors=3) blended 20 percent with the KNN prediction and 80 percent with the train mean",
            "split": "development rows train, Molicell subset holdout, no random row split",
            "kk_screen": "finite-range RC-basis Kramer-Kronig residual check on holdout EIS targets",
            "preprocessing": "median imputation and standard scaling inside a scikit-learn ColumnTransformer",
            "derived_features": "log duration, voltage delta/range/CV, current load factor, total/net throughput, discharge-to-charge ratio",
        },
        "results": {
            "baseline_rmse_all_ohm": baseline_metrics["rmse_all_ohm"],
            "model_rmse_all_ohm": model_metrics["rmse_all_ohm"],
            "baseline_metrics": baseline_metrics,
            "model_metrics": model_metrics,
            "per_frequency_rmse_ohm": per_frequency_error_payload(pairs, targets, test_y, baseline_pred, model_pred),
            "representative_spectrum": representative_spectrum(test, pairs, targets, baseline_pred, model_pred),
            "relative_rmse_improvement_fraction": improvement,
            "demo_verdict": "working_demo_model_beats_baseline" if improvement > 0 else "working_demo_no_support",
            "kk_valid_fraction": kk_summary["kk_valid_fraction"],
            "kk_valid_rows": kk_summary["kk_valid_rows"],
            "kk_rows_checked": kk_summary["rows_checked"],
            "kk_summary": kk_summary,
            "kk_preview_rows": records_preview(kk_rows, list(kk_rows.columns), rows=5),
        },
        "outputs": {
            "results_json": str(DEMO_RESULTS_JSON),
            "presentation_html": str(DEMO_PRESENTATION_HTML),
            "code_bundle": str(DEMO_CODE_BUNDLE),
            "data_bundle": str(DEMO_DATA_BUNDLE),
        },
    }
    return results

# 2. Time-domain derived features.

def add_derived_features(frame: pd.DataFrame) -> pd.DataFrame:
    """Add time-domain-only features without touching target-side EIS values."""

    frame = frame.copy()
    for col in BASE_FEATURE_COLUMNS:
        if col not in frame.columns:
            frame[col] = np.nan
        frame[col] = pd.to_numeric(frame[col], errors="coerce")

    voltage_mean_abs = frame["td_voltage_mean_v"].abs().replace(0, np.nan)
    duration_hours = (frame["td_duration_s"] / 3600.0).replace(0, np.nan)
    charge = frame["td_charge_throughput_ah"].clip(lower=0)
    discharge = frame["td_discharge_throughput_ah"].clip(lower=0)
    total_throughput = charge + discharge

    frame["td_rows_log1p"] = np.log1p(frame["td_rows"].clip(lower=0))
    frame["td_duration_log1p_s"] = np.log1p(frame["td_duration_s"].clip(lower=0))
    frame["td_voltage_delta_v"] = frame["td_voltage_end_v"] - frame["td_voltage_start_v"]
    frame["td_voltage_range_v"] = frame["td_voltage_max_v"] - frame["td_voltage_min_v"]
    frame["td_voltage_cv"] = safe_divide(frame["td_voltage_std_v"], voltage_mean_abs)
    frame["td_current_activity_span_a"] = frame["td_current_abs_max_a"] - frame["td_current_abs_mean_a"]
    frame["td_current_load_factor"] = safe_divide(frame["td_current_abs_mean_a"], frame["td_current_abs_max_a"].replace(0, np.nan))
    frame["td_total_throughput_ah"] = total_throughput
    frame["td_net_throughput_ah"] = charge - discharge
    frame["td_discharge_to_charge_ratio"] = safe_divide(discharge, charge.replace(0, np.nan))
    frame["td_mean_abs_current_per_hour"] = safe_divide(frame["td_current_abs_mean_a"], duration_hours)
    return frame

# 3. Model preprocessing and estimator wrapper.

def build_model(estimator: Any, feature_columns: list[str] | None = None) -> Pipeline:
    columns = feature_columns or FEATURE_COLUMNS
    preprocessor = ColumnTransformer(
        [
            (
                "numeric",
                Pipeline(
                    [
                        ("impute", SimpleImputer(strategy="median")),
                        ("scale", StandardScaler()),
                    ]
                ),
                columns,
            )
        ]
    )
    return Pipeline([("preprocess", preprocessor), ("model", estimator)])

# 4. Metric calculation.

def metric_payload(y_true: np.ndarray, y_pred: np.ndarray, target_cols: list[str]) -> dict[str, Any]:
    zreal_idx = [idx for idx, col in enumerate(target_cols) if "zreal" in col]
    znegimag_idx = [idx for idx, col in enumerate(target_cols) if "znegimag" in col]
    per_target = {
        col: float(mean_squared_error(y_true[:, idx], y_pred[:, idx]) ** 0.5)
        for idx, col in enumerate(target_cols)
    }
    payload = {
        "rmse_all_ohm": float(mean_squared_error(y_true.ravel(), y_pred.ravel()) ** 0.5),
        "mae_all_ohm": float(mean_absolute_error(y_true.ravel(), y_pred.ravel())),
        "bias_all_ohm": float(np.mean(y_pred - y_true)),
        "rmse_zreal_ohm": float(mean_squared_error(y_true[:, zreal_idx].ravel(), y_pred[:, zreal_idx].ravel()) ** 0.5),
        "rmse_znegimag_ohm": float(
            mean_squared_error(y_true[:, znegimag_idx].ravel(), y_pred[:, znegimag_idx].ravel()) ** 0.5
        ),
        "r2_uniform_average": float(r2_score(y_true, y_pred, multioutput="uniform_average")),
        "per_target_rmse_ohm": per_target,
    }
    return payload

# 5. Kramer-Kronig target-quality screen.

def validate_matrix(
    frame: pd.DataFrame,
    matrix_name: str,
    residual_limit: float = DEFAULT_RESIDUAL_LIMIT,
    max_rows: int = 0,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    frequencies, zreal_cols, znegimag_cols = fixed_grid_columns(list(frame.columns))
    if not frequencies:
        raise RuntimeError(f"No fixed-grid EIS target columns found for {matrix_name}.")

    work = frame.copy()
    if max_rows > 0:
        work = work.head(max_rows).copy()

    rows: list[dict[str, Any]] = []
    for idx, row in work.iterrows():
        metrics = validate_spectrum(
            frequencies,
            [row[col] for col in zreal_cols],
            [row[col] for col in znegimag_cols],
            residual_limit=residual_limit,
        )
        rows.append(
            {
                "matrix": matrix_name,
                "row_index": int(idx) if isinstance(idx, (int, np.integer)) else str(idx),
                "sample_id": str(row.get("sample_id", "")),
                "dataset": str(row.get("dataset", "")),
                "split_role": str(row.get("split_role", "")),
                "cell_id": str(row.get("cell_id", "")),
                "temperature_c": row.get("temperature_c", np.nan),
                "soc_percent": row.get("soc_percent", np.nan),
                **metrics,
            }
        )

    result = pd.DataFrame(rows)
    status_counts = Counter(result["kk_status"].astype(str)) if not result.empty else Counter()
    valid_count = int(result["kk_valid"].sum()) if "kk_valid" in result else 0
    residual_values = pd.to_numeric(result.get("kk_residual_norm", pd.Series(dtype=float)), errors="coerce")
    summary = {
        "matrix": matrix_name,
        "rows_checked": int(len(result)),
        "kk_valid_rows": valid_count,
        "kk_valid_fraction": float(valid_count / len(result)) if len(result) else 0.0,
        "kk_status_counts": dict(sorted(status_counts.items())),
        "kk_residual_norm_median": float(residual_values.median()) if residual_values.notna().any() else None,
        "kk_residual_norm_p95": float(residual_values.quantile(0.95)) if residual_values.notna().any() else None,
        "kk_residual_limit": float(residual_limit),
        "frequency_grid_hz": frequencies,
        "claim_boundary": (
            "Finite-range RC-basis Kramer-Kronig consistency screen. Use as EIS quality metadata, "
            "not as proof that a prediction model is valid."
        ),
    }
    return result, summary
