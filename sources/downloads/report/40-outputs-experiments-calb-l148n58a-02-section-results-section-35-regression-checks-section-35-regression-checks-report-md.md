# CALB L148N58A, regression checks Regression Checks

## Purpose

Lock the current CALB bridge baseline so future edits do not silently break the professor-facing claim.

## Result

- Checks passed: 49 / 49
- Nonzero section error counts: 0
- Nonempty error CSVs: 0
- Verdict: `calb_core_regression_checks_pass`

## Checks

| Check | Status | Observed | Expected |
| --- | --- | --- | --- |
| section33_row_count | PASS | 246 | 246 |
| section33_quality_pass_rows | PASS | 246 | 246 |
| section33_error_count | PASS | 0 | 0 |
| section33_fallback_rows_exact | PASS | 2 | 2 |
| section33_lambda_sequence | PASS | [3.0, 0.1] | [3.0, 0.1] |
| section33_verdict | PASS | adaptive_final_rule_all_temperatures_all_rows_pass | adaptive_final_rule_all_temperatures_all_rows_pass |
| section33_rows_csv_count | PASS | 246 | 246 |
| section33_all_rows_quality_pass | PASS | all true | all true |
| section33_fallback_identity | PASS | [('59861', 40, 'HPPC_1C', 1, 15, 0.1), ('59861', 40, 'HPPC_C3', 1, 15, 0.1)] | [('59861', 40, 'HPPC_1C', 1, 15, 0.1), ('59861', 40, 'HPPC_C3', 1, 15, 0.1)] |
| section33_fallback_rule | PASS | ['fallback_lambda_corr_only'] | ['fallback_lambda_corr_only'] |
| section33_all_temperatures_full_pass | PASS | rows == pass rows | rows == pass rows |
| section29_error_count | PASS | 0 | 0 |
| section29_missing_eis_skips | PASS | 3 | 3 |
| section34_error_count | PASS | 0 | 0 |
| section34_row_count | PASS | 198 | 198 |
| section34_drt_win_fraction | PASS | 1.0 | 1.0 |
| section36_error_count | PASS | 0 | 0 |
| section36_row_count | PASS | 198 | 198 |
| section36_verdict | PASS | drive_cycle_ecm_baseline_beats_fixed_drt | drive_cycle_ecm_baseline_beats_fixed_drt |
| section36_drt_loses_best_ecm_median | PASS | 3.0704702158353285 | > 0 mV |
| section36_drt_win_fraction_low | PASS | 0.12121212121212122 | < 0.5 |
| section37_error_count | PASS | 0 | 0 |
| section37_verdict | PASS | soc_alignment_audit_complete | soc_alignment_audit_complete |
| section37_bridge_alignment_tight | PASS | 0 | 0 |
| section37_drive_alignment_bad | PASS | 182 | > 0 |
| section37_drive_alignment_median_bad | PASS | 0.0637559086707088 | > 0.05 SOC fraction |
| section38_verdict | PASS | uncertainty_audit_complete | uncertainty_audit_complete |
| section38_metric_count | PASS | 12 | 12 |
| section38_has_drive_ecm_interval | PASS | ['section33_fallback_fraction', 'section33_median_abs_ocv_delta_v_quality', 'section33_median_corr_quality', 'section33_median_time_rmse_mv_quality', 'section36_drt_win_fraction_vs_best_ecm', 'section36_median_best_ecm_holdout_rmse_mv', 'section36_median_drt_holdout_rmse_mv', 'section36_median_drt_minus_best_ecm_rmse_mv', 'section37_bridge_soc_delta_gt_2pct_fraction', 'section37_drive_soc_delta_gt_5pct_fraction', 'section37_median_bridge_abs_soc_delta', 'section37_median_drive_abs_soc_delta'] | section36_median_drt_minus_best_ecm_rmse_mv present |
| section38_has_soc_interval | PASS | ['section33_fallback_fraction', 'section33_median_abs_ocv_delta_v_quality', 'section33_median_corr_quality', 'section33_median_time_rmse_mv_quality', 'section36_drt_win_fraction_vs_best_ecm', 'section36_median_best_ecm_holdout_rmse_mv', 'section36_median_drt_holdout_rmse_mv', 'section36_median_drt_minus_best_ecm_rmse_mv', 'section37_bridge_soc_delta_gt_2pct_fraction', 'section37_drive_soc_delta_gt_5pct_fraction', 'section37_median_bridge_abs_soc_delta', 'section37_median_drive_abs_soc_delta'] | section37_drive_soc_delta_gt_5pct_fraction present |
| section39_verdict | PASS | external_replication_blocked_missing_corrected_eis | external_replication_blocked_missing_corrected_eis |
| section39_not_ready | PASS | False | False |
| section39_blocker_count | PASS | 3 | 3 |
| section39_blocker_identity | PASS | ['dib_overlap_too_small', 'kit_local_eis_archive_incomplete', 'zenodo_expt4_no_same_cell_eis'] | ['dib_overlap_too_small', 'kit_local_eis_archive_incomplete', 'zenodo_expt4_no_same_cell_eis'] |
| section40_verdict | PASS | local_leakage_and_claim_limits_documented | local_leakage_and_claim_limits_documented |
| section40_high_risk_items | PASS | 5 | 5 |
| section40_claim_boundary | PASS | internal_engineering_result_not_clean_holdout_or_external_validation | internal_engineering_result_not_clean_holdout_or_external_validation |
| section41_verdict | PASS | local_ablation_evidence_consolidated_not_external_validation | local_ablation_evidence_consolidated_not_external_validation |
| section41_ablation_count | PASS | 12 | 12 |
| section41_has_tau_constraint | PASS | ['cold_eis_window', 'cold_time_window', 'drive_cycle_soc_alignment', 'drive_cycle_stronger_ecm_baseline', 'final_10c_rule', 'fixed_multitemp_rule', 'narrow_eis_lambda_fallback', 'protocol_replication_hppc_1c_c3', 'record3_short_hppc_candidate', 'regularization_only_cold_fix', 'reject_far_ocv_rescue', 'tau_support_constraint'] | tau_support_constraint present |
| section41_has_drive_soc_limit | PASS | ['cold_eis_window', 'cold_time_window', 'drive_cycle_soc_alignment', 'drive_cycle_stronger_ecm_baseline', 'final_10c_rule', 'fixed_multitemp_rule', 'narrow_eis_lambda_fallback', 'protocol_replication_hppc_1c_c3', 'record3_short_hppc_candidate', 'regularization_only_cold_fix', 'reject_far_ocv_rescue', 'tau_support_constraint'] | drive_cycle_soc_alignment present |
| section42_verdict | PASS | drive_cycle_result_soc_misaligned_and_ecm_baseline_still_stronger | drive_cycle_result_soc_misaligned_and_ecm_baseline_still_stronger |
| section42_row_count | PASS | 198 | 198 |
| section42_aligned_rows_sparse | PASS | 16 | 16 |
| section42_no_missing_soc_rows | PASS | 0 | 0 |
| section42_aligned_drt_win_fraction_zero | PASS | 0.0 | 0.0 |
| section42_has_misaligned_bucket | PASS | ['gt_10pct', 'gt_2_to_5pct', 'gt_5_to_10pct'] | gt_5_to_10pct present |
| all_section_error_counts_zero | PASS | 0 | 0 |
| all_error_csvs_empty | PASS | 0 | 0 |

## Error Scan

- No nonzero `error_count` values found in CALB section summaries.
- No nonempty CALB `*errors*.csv` files found.

## Blunt Read

This only locks internal consistency. It does not prove aging, SOH, external replication, or the combined EIS/TDM objective.

## Outputs

- `section_35_checks.csv`
- `section_35_nonempty_error_files.csv`
- `section_35_nonzero_error_counts.csv`
- `section_35_summary.json`
