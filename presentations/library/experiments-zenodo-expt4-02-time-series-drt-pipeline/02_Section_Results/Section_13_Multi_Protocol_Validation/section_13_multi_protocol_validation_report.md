# LG M50T 21700 Expt 4 drive-cycle aging Time-Series DRT Pipeline, multi-temperature 2D batch check

## Purpose

This section combines GITT, discharge-curve, and hybrid-pulse features into one held-out-cell health-label validation table.

## Results

- Feature table rows: 80
- Prediction rows: 600
- Metric rows: 11
- Feature counts: `{"all_protocols": 80, "discharge_only": 26, "gitt_only": 32, "hybrid_only": 22}`
- Target-proxy features excluded: 64
- Leakage audit: `section_13_feature_leakage_audit.csv`

## Best Skill Rows

- resistance_0p1s_ohm / all_protocols: MAE 0.0002813, baseline MAE 0.001851, skill 0.848
- c10_capacity_mah / gitt_only: MAE 39.42, baseline MAE 242.9, skill 0.838
- resistance_0p1s_ohm / gitt_only: MAE 0.0003902, baseline MAE 0.001851, skill 0.789
- soh / gitt_only: MAE 0.01127, baseline MAE 0.04926, skill 0.771
- soh / discharge_only: MAE 0.01151, baseline MAE 0.04947, skill 0.767
- c10_capacity_mah / discharge_only: MAE 58.13, baseline MAE 244.7, skill 0.762
- c10_capacity_mah / all_protocols: MAE 75.05, baseline MAE 244.7, skill 0.693
- resistance_0p1s_ohm / discharge_only: MAE 0.0005692, baseline MAE 0.001851, skill 0.693
- soh / all_protocols: MAE 0.01544, baseline MAE 0.04947, skill 0.688
- soh / hybrid_only: MAE 0.02992, baseline MAE 0.05018, skill 0.404

## Interpretation

This is the closest version of a full LG M50T 21700 Expt 4 drive-cycle aging pipeline so far.
It uses all processed families, but it still keeps DRT claims limited to the GITT-derived track.
If all-protocol features beat GITT-only and discharge-only features after proxy exclusion, then the rest of the Zenodo package is adding real exploratory value.
Capacity, capacity-normalized duration, capacity-axis voltage, hybrid transition-count, and hybrid segment-duration/count features are excluded for SOH/C10 targets.
Do not compare these cleaned scores with the old near-perfect C10 result. That old result was leakage-shaped, not impressive.
