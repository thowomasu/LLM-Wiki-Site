# LG M50T 21700 Expt 4 drive-cycle aging Time-Series DRT Pipeline, multi-temperature 2D batch check

## Purpose

This section combines GITT, discharge-curve, and hybrid-pulse features into one held-out-cell health-label validation table.

## Results

- Feature table rows: 80
- Prediction rows: 600
- Metric rows: 11
- Feature counts: `{"all_protocols": 26, "discharge_only": 10, "gitt_only": 6, "hybrid_only": 10}`
- Target-proxy features excluded: 16
- Leakage audit: `section_13_feature_leakage_audit.csv`

## Best Skill Rows

- c10_capacity_mah / hybrid_only: MAE 25.56, baseline MAE 248.7, skill 0.897
- soh / hybrid_only: MAE 0.006115, baseline MAE 0.05018, skill 0.878
- resistance_0p1s_ohm / gitt_only: MAE 0.0005195, baseline MAE 0.001851, skill 0.719
- soh / all_protocols: MAE 0.01755, baseline MAE 0.04947, skill 0.645
- c10_capacity_mah / all_protocols: MAE 88, baseline MAE 244.7, skill 0.64
- c10_capacity_mah / discharge_only: MAE 130.4, baseline MAE 244.7, skill 0.467
- soh / discharge_only: MAE 0.02667, baseline MAE 0.04947, skill 0.461
- resistance_0p1s_ohm / all_protocols: MAE 0.001012, baseline MAE 0.001851, skill 0.453
- soh / gitt_only: MAE 0.0284, baseline MAE 0.04926, skill 0.423
- resistance_0p1s_ohm / discharge_only: MAE 0.001081, baseline MAE 0.001851, skill 0.416

## Interpretation

This is the closest version of a full LG M50T 21700 Expt 4 drive-cycle aging pipeline so far.
It uses all processed families, but it still keeps DRT claims limited to the GITT-derived track.
If all-protocol features beat GITT-only and discharge-only features, then the rest of the Zenodo package is adding real value.
Capacity-proxy discharge features are now excluded when the target is `soh` or `c10_capacity_mah`. The old near-perfect C10 result was leakage-shaped, not impressive.
