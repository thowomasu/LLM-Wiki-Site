# LG M50T 21700 Expt 4 drive-cycle aging failure-mode audit, Negative Controls

## Purpose

This section tests whether the locked combined DRT mirror check feature sets beat shuffled-label controls.
It does not validate EIS DRT. It only asks whether the health-label signal is stronger than a simple label-randomization baseline.

## Verdict

- Shuffle-control checks passed: 18 of 18
- Permutations per check: 200

Passing a shuffle control means the original held-out skill is above the 95th percentile of shuffled-label skill for the same target, split, and feature set.

## Strong Rows

| validation | target | feature_set | original_skill | original_mae | permutation_count | permutation_skill_median | permutation_skill_p95 | permutation_skill_max | empirical_p_perm_ge_original | original_beats_permutation_p95 | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| leave_one_cell_out | soh | r0_plus_drt_bands | 0.495061 | 0.0248732 | 200 | -0.146661 | -0.0184589 | 0.0815841 | 0 | True | passes_shuffle_control |
| leave_one_cell_out | resistance_0p1s_ohm | r0_plus_drt_bands | 0.821437 | 0.00033056 | 200 | -0.114853 | 0.00236701 | 0.104262 | 0 | True | passes_shuffle_control |
| leave_one_cell_out | c10_capacity_mah | r0_plus_drt_bands | 0.485665 | 124.926 | 200 | -0.134496 | -0.0157385 | 0.0513032 | 0 | True | passes_shuffle_control |
| leave_one_temperature_out | soh | r0_plus_drt_bands | 0.419729 | 0.0285945 | 200 | -0.266729 | -0.0251429 | 0.103778 | 0 | True | passes_shuffle_control |
| leave_one_temperature_out | resistance_0p1s_ohm | r0_plus_drt_bands | 0.786109 | 0.000406147 | 200 | -0.23713 | -0.00389991 | 0.156473 | 0 | True | passes_shuffle_control |
| leave_one_temperature_out | c10_capacity_mah | r0_plus_drt_bands | 0.415433 | 141.525 | 200 | -0.247085 | 0.00506941 | 0.111623 | 0 | True | passes_shuffle_control |

## Weak Or Failed Rows

No rows.

## Original Metrics Recomputed

| n | mae | rmse | baseline_mae | skill_vs_baseline_mae | validation | target | feature_set | features_used |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | 0.029643 | 0.0462197 | 0.0492598 | 0.398232 | leave_one_cell_out | soh | r0_only | 1 |
| 40 | 0.0285442 | 0.0550742 | 0.0492598 | 0.420537 | leave_one_cell_out | soh | drt_bands_only | 3 |
| 40 | 0.0248732 | 0.0387601 | 0.0492598 | 0.495061 | leave_one_cell_out | soh | r0_plus_drt_bands | 4 |
| 40 | 0.000283969 | 0.000450366 | 0.00185122 | 0.846605 | leave_one_cell_out | resistance_0p1s_ohm | r0_only | 1 |
| 40 | 0.00140265 | 0.00216269 | 0.00185122 | 0.242308 | leave_one_cell_out | resistance_0p1s_ohm | drt_bands_only | 3 |
| 40 | 0.00033056 | 0.000594893 | 0.00185122 | 0.821437 | leave_one_cell_out | resistance_0p1s_ohm | r0_plus_drt_bands | 4 |
| 40 | 153.444 | 231.267 | 242.887 | 0.368249 | leave_one_cell_out | c10_capacity_mah | r0_only | 1 |
| 40 | 140.526 | 275.548 | 242.887 | 0.421436 | leave_one_cell_out | c10_capacity_mah | drt_bands_only | 3 |
| 40 | 124.926 | 205.958 | 242.887 | 0.485665 | leave_one_cell_out | c10_capacity_mah | r0_plus_drt_bands | 4 |
| 40 | 0.0288477 | 0.0438349 | 0.0492778 | 0.414591 | leave_one_temperature_out | soh | r0_only | 1 |
| 40 | 0.0341128 | 0.0673346 | 0.0492778 | 0.307746 | leave_one_temperature_out | soh | drt_bands_only | 3 |
| 40 | 0.0285945 | 0.0496732 | 0.0492778 | 0.419729 | leave_one_temperature_out | soh | r0_plus_drt_bands | 4 |
| 40 | 0.000385635 | 0.000587624 | 0.00189884 | 0.796911 | leave_one_temperature_out | resistance_0p1s_ohm | r0_only | 1 |
| 40 | 0.00160097 | 0.00257702 | 0.00189884 | 0.156869 | leave_one_temperature_out | resistance_0p1s_ohm | drt_bands_only | 3 |
| 40 | 0.000406147 | 0.000680834 | 0.00189884 | 0.786109 | leave_one_temperature_out | resistance_0p1s_ohm | r0_plus_drt_bands | 4 |
| 40 | 149.89 | 221.416 | 242.102 | 0.38088 | leave_one_temperature_out | c10_capacity_mah | r0_only | 1 |
| 40 | 166.155 | 324.639 | 242.102 | 0.3137 | leave_one_temperature_out | c10_capacity_mah | drt_bands_only | 3 |
| 40 | 141.525 | 243.528 | 242.102 | 0.415433 | leave_one_temperature_out | c10_capacity_mah | r0_plus_drt_bands | 4 |

## Interpretation

If a locked feature row fails this control, do not use it as evidence.
Rows that pass are still only Expt4 health-feature evidence, not EIS validation.
The next useful check is a wrong-window control if the source window tables preserve enough candidate information.

## Outputs

- `section_15_original_metrics_recomputed.csv`
- `section_15_shuffled_label_metrics.csv`
- `section_15_shuffle_control_summary.csv`
- `section_15_negative_controls_summary.json`
