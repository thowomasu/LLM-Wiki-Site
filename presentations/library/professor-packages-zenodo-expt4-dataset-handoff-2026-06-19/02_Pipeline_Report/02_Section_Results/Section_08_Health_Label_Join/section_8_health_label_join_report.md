# LG M50T 21700 Expt 4 drive-cycle aging Time-Series DRT Pipeline, combined EIS and time-domain DRT prototype

## Purpose

This section joins fitted GITT DRT-like features to Experiment 4 health labels.
This is the first section that asks whether the features track ageing labels instead of merely fitting voltage.

## Inputs

- Batch feature table: `[local path redacted]`

## Outputs

- `section_8_health_label_join_results.csv`
- `section_8_feature_label_correlations.csv`
- `section_8_health_label_join_summary.json`
- `section_8_health_label_join.png`

## Results

- Joined rows: 40
- Cells: `A, B, C, D, E, F, G, H`
- RPTs: `0, 2, 4, 6, 8`
- Correlations computed: 63

## Strongest Correlations

- r0_ohm vs resistance_0p1s_ohm: Spearman 0.971, Pearson 0.972, n=40
- r0_ohm vs soh: Spearman -0.877, Pearson -0.788, n=40
- r0_ohm vs charge_throughput_ah: Spearman 0.860, Pearson 0.742, n=40
- r0_ohm vs energy_throughput_wh: Spearman 0.859, Pearson 0.742, n=40
- r0_ohm vs days_degradation: Spearman 0.853, Pearson 0.747, n=40
- r0_ohm vs c2_capacity_mah: Spearman -0.847, Pearson -0.763, n=40
- r0_ohm vs c10_capacity_mah: Spearman -0.846, Pearson -0.776, n=40
- rmse_mv vs days_degradation: Spearman 0.522, Pearson 0.430, n=40

## Interpretation

This is useful, but do not overread it.
These are same-dataset associations from selected GITT windows, not proof that the recovered DRT spectrum is physically correct.
The next hard test is held-out-cell prediction inside temperature groups, because cross-temperature pooling can create fake-looking correlations.
