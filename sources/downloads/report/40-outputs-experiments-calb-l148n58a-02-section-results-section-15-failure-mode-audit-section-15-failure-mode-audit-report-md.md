# CALB L148N58A, failure-mode audit Failure Mode Audit

## Purpose

Find where the combined DRT mirror check combined DRT mirror helps, where it damages the result, and what that implies for the next pipeline change.

## Headline

- Quality-pass rows: 71 of 123.
- Combined better rows: 53.
- Large gain rows: 11.
- Large loss rows: 16.
- Median delta, high OCV: 0.030321548537452.
- Median delta, low OCV: 0.0093846055296428.

## EIS/OCV Band Summary

| OCV band | Rows | Quality-pass | Separate corr | Combined corr | Delta corr | Large gains | Large losses |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| high_ocv | 33 | 22 | -0.054073941791552296 | -0.01936372131136785 | 0.030321548537452 | 5 | 0 |
| mid_ocv | 33 | 24 | -0.047348892529577954 | -0.0046589419609603 | 0.0357350972588439 | 5 | 6 |
| low_ocv | 33 | 25 | -0.0349117182476623 | -0.0155750018306159 | 0.0093846055296428 | 1 | 10 |
| extra_low_ocv | 24 | 0 | None | None | None | 0 | 0 |

## Quality Gate Failures

- combined_eis_real_rmse_gt_0p2mohm: 34
- combined_time_rmse_gt_10mv: 30
- separate_time_rmse_gt_10mv: 22
- combined_eis_img_rmse_gt_0p2mohm: 19
- ocv_delta_gt_20mv: 10

## Blunt Read

The combined objective is not uniformly better. It has enough signal to keep investigating, but it also destroys some rows that the separate time-domain fit handled well.
That means the next engineering move should be targeted, not broader batching.

## Next Move

Build a weighting and alignment experiment for the low-OCV records. Do not rerun the whole dataset until a small controlled subset improves without wrecking the already-good separate rows.

## Outputs

- `section_15_by_ocv_band.csv`
- `section_15_by_temperature.csv`
- `section_15_by_cell.csv`
- `section_15_failure_flags.csv`
- `section_15_correlations.csv`
- `section_15_best_gain_rows.csv`
- `section_15_worst_loss_rows.csv`
- `section_15_summary.json`

## Linked Graph

![failure-mode audit failure mode audit](section_15_failure_mode_audit.png)
