# LG M50T 21700 Expt 4 drive-cycle aging Time-Series DRT Pipeline, time-series 2D DRT surface

## Purpose

This section tests whether the fitted GITT features survive a simple held-out-cell check.
The model is deliberately small ridge regression. A fancier model on 40 rows would be noise cosplay.

## Outputs

- `section_9_held_out_cell_predictions.csv`
- `section_9_held_out_cell_metrics.csv`
- `section_9_drt_incremental_value.csv`
- `section_9_held_out_cell_validation_summary.json`
- `section_9_held_out_cell_validation.png`

## Results

- Input rows: 40
- Prediction rows: 1260
- Metric rows: 36
- Incremental-value rows: 18
- DRT over R0+voltage positive rows: 2

## Best Skill Rows

- within_temperature / resistance_0p1s_ohm / r0_only: MAE 0.0003941, baseline MAE 0.002057, skill 0.808
- global / resistance_0p1s_ohm / drt_plus_r0_voltage: MAE 0.0004248, baseline MAE 0.001851, skill 0.771
- global / resistance_0p1s_ohm / r0_only: MAE 0.0004644, baseline MAE 0.001851, skill 0.749
- global / resistance_0p1s_ohm / r0_plus_voltage: MAE 0.0004699, baseline MAE 0.001851, skill 0.746
- within_temperature / resistance_0p1s_ohm / drt_plus_r0: MAE 0.0005231, baseline MAE 0.002057, skill 0.746
- global / resistance_0p1s_ohm / drt_plus_r0: MAE 0.0005212, baseline MAE 0.001851, skill 0.718
- within_temperature / resistance_0p1s_ohm / drt_plus_r0_voltage: MAE 0.001076, baseline MAE 0.002057, skill 0.477
- within_temperature / c10_capacity_mah / drt_plus_r0: MAE 147.4, baseline MAE 277.3, skill 0.468

## DRT Incremental Value

- global / soh: MAE delta -0.003602, skill delta -0.0731, augmented better=False
- global / resistance_0p1s_ohm: MAE delta 4.509e-05, skill delta 0.0244, augmented better=True
- global / c10_capacity_mah: MAE delta -15.91, skill delta -0.0655, augmented better=False
- within_temperature / soh: MAE delta -0.065, skill delta -1.16, augmented better=False
- within_temperature / resistance_0p1s_ohm: MAE delta 7.339e-05, skill delta 0.0357, augmented better=True
- within_temperature / c10_capacity_mah: MAE delta -333, skill delta -1.2, augmented better=False

## Interpretation

Positive skill means the feature set beat a train-mean baseline. Negative skill means it made things worse.
This is the closest honest replacement for DIB EIS validation in Expt4. It validates health-feature usefulness, not DRT physics.
If global validation works but within-temperature validation collapses, the model is mostly learning temperature grouping. Do not hide that.
If DRT bands do not improve over R0 plus simple voltage features, they are not ready to justify a larger model.
