# LG M50T 21700 Expt 4 drive-cycle aging Viability Report

## Verdict

- Engineering scaffold: health_feature_scaffold_viable
- Scientific method: not_eis_validated

Plain English: this package is now viable as a multi-protocol health-feature pipeline on LG M50T 21700 Expt 4 drive-cycle aging data.
It is not viable as EIS-validated DRT physics, because this dataset track still lacks paired EIS-derived DRT targets.

## What Passes

- Full 25-pulse GITT batch: 40 files completed, 0 errors.
- Discharge-curve feature extraction: 120 files completed, 0 errors.
- Hybrid-pulse feature extraction: 80 files completed, 0 errors.
- Health-label join: 40 rows across cells A-H and RPT 0, 2, 4, 6, 8.
- GITT held-out-cell validation: 1260 prediction rows.
- Multi-protocol held-out-cell validation: 600 prediction rows.
- Leakage guard: 16 target-proxy feature uses excluded from multi-temperature 2D batch check.
- Trend consistency: expected-direction pass ratio 0.875.

## Best GITT Held-Out Signals

- within_temperature / resistance_0p1s_ohm / r0_only: MAE 0.0003941, baseline MAE 0.002057, skill 0.808
- global / resistance_0p1s_ohm / drt_plus_r0_voltage: MAE 0.0004248, baseline MAE 0.001851, skill 0.771
- global / resistance_0p1s_ohm / r0_only: MAE 0.0004644, baseline MAE 0.001851, skill 0.749
- global / resistance_0p1s_ohm / r0_plus_voltage: MAE 0.0004699, baseline MAE 0.001851, skill 0.746
- within_temperature / resistance_0p1s_ohm / drt_plus_r0: MAE 0.0005231, baseline MAE 0.002057, skill 0.746
- global / resistance_0p1s_ohm / drt_plus_r0: MAE 0.0005212, baseline MAE 0.001851, skill 0.718
- within_temperature / resistance_0p1s_ohm / drt_plus_r0_voltage: MAE 0.001076, baseline MAE 0.002057, skill 0.477
- within_temperature / c10_capacity_mah / drt_plus_r0: MAE 147.4, baseline MAE 277.3, skill 0.468

## DRT Incremental Value

- DRT bands improved over R0 plus simple voltage features in 2 of 6 target/scope checks.
- global / soh: MAE delta -0.003602, skill delta -0.0731, augmented better=False
- global / resistance_0p1s_ohm: MAE delta 4.509e-05, skill delta 0.0244, augmented better=True
- global / c10_capacity_mah: MAE delta -15.91, skill delta -0.0655, augmented better=False
- within_temperature / soh: MAE delta -0.065, skill delta -1.16, augmented better=False
- within_temperature / resistance_0p1s_ohm: MAE delta 7.339e-05, skill delta 0.0357, augmented better=True
- within_temperature / c10_capacity_mah: MAE delta -333, skill delta -1.2, augmented better=False

## Best Multi-Protocol Held-Out Signals

- c10_capacity_mah / hybrid_only: MAE 25.56, baseline MAE 248.7, skill 0.897
- soh / hybrid_only: MAE 0.006115, baseline MAE 0.05018, skill 0.878
- resistance_0p1s_ohm / gitt_only: MAE 0.0005195, baseline MAE 0.001851, skill 0.719
- soh / all_protocols: MAE 0.01755, baseline MAE 0.04947, skill 0.645
- c10_capacity_mah / all_protocols: MAE 88, baseline MAE 244.7, skill 0.64
- c10_capacity_mah / discharge_only: MAE 130.4, baseline MAE 244.7, skill 0.467
- soh / discharge_only: MAE 0.02667, baseline MAE 0.04947, skill 0.461
- resistance_0p1s_ohm / all_protocols: MAE 0.001012, baseline MAE 0.001851, skill 0.453

## What Still Fails Scientifically

- No EIS-derived DRT comparison target was found in the inspected Expt4 folders.
- The strongest held-out result is mostly R0 predicting the 0.1s resistance label. Useful, but not surprising.
- Discharge-derived capacity features are excluded for SOH and C10 capacity targets because they are target proxies. Good science sometimes means deleting your best-looking number.
- DRT band features only beat R0 plus simple voltage features in 2 of 6 checked cases. That is weak, not a green light.
- Discharge and hybrid features help make the Zenodo package usable, but they are not DRT evidence.
- Temperature grouping can create fake-looking global structure. Within-temperature validation matters more.

## Do Next

1. Do not train a larger model yet. The DRT-band incremental signal is too inconsistent.
2. Fit all accepted GITT pulses per file, then aggregate by SOC/pulse index instead of relying on one selected pulse.
3. Upgrade hybrid pulse segmentation before trying hybrid DRT.
4. Only claim DRT physics if a matched EIS source is added later.

Blunt version: LG M50T 21700 Expt 4 drive-cycle aging is now a real multi-protocol health-feature scaffold. It is still not a substitute for the DIB EIS validation track.
