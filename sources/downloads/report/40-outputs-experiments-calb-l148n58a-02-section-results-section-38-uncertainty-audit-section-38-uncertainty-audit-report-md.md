# CALB L148N58A, analysis step 38 Uncertainty Audit

## Purpose

Bootstrap the saved row-level outputs so the final claims have uncertainty intervals instead of single-number theater.

## Result

- Bootstrap samples per metric: 5000
- Metrics audited: 12
- Random seed: 20260624
- Verdict: `uncertainty_audit_complete`

## Intervals

| Metric | Median | 2.5% | 97.5% |
| --- | ---: | ---: | ---: |
| section33_median_corr_quality | 0.9281925850569117 | 0.9280384935823768 | 0.9283595082110088 |
| section33_median_abs_ocv_delta_v_quality | 0.00329664891052235 | 0.0026070705261229503 | 0.0037896584625242502 |
| section33_median_time_rmse_mv_quality | 3.144651471038199 | 3.0049324835472406 | 3.415856589726491 |
| section33_fallback_fraction | 0.008130081300813009 | 0.0 | 0.02032520325203252 |
| section36_median_drt_holdout_rmse_mv | 150.9172295922953 | 145.98912318036656 | 153.06513820450715 |
| section36_median_best_ecm_holdout_rmse_mv | 134.8626012268972 | 131.3682325483028 | 139.15952579779596 |
| section36_median_drt_minus_best_ecm_rmse_mv | 3.0704702158353285 | 2.9206679021260555 | 4.964587444670613 |
| section36_drt_win_fraction_vs_best_ecm | 0.12121212121212122 | 0.07575757575757576 | 0.16666666666666666 |
| section37_median_bridge_abs_soc_delta | 0.00455600361301455 | 0.0041061138343089 | 0.005536122576838182 |
| section37_bridge_soc_delta_gt_2pct_fraction | 0.0 | 0.0 | 0.0 |
| section37_median_drive_abs_soc_delta | 0.0637559086707088 | 0.0605070770628998 | 0.0682959167262021 |
| section37_drive_soc_delta_gt_5pct_fraction | 0.9191919191919192 | 0.8787878787878788 | 0.9545454545454546 |

## Blunt Read

The uncertainty bands do not rescue weak claims. They make the weak claims harder to hide. In particular, drive-cycle ECM baseline check's fixed-DRT loss to best ECM should be treated as a real internal warning unless a stronger aligned rerun reverses it.

## Outputs

- `section_38_bootstrap_intervals.csv`
- `section_38_summary.json`
