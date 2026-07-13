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
- GITT held-out-cell validation: 990 prediction rows.
- Multi-protocol held-out-cell validation: 600 prediction rows.
- Locked R0-vs-DRT validation: 720 prediction rows.
- Leakage guard: 64 target-proxy feature uses excluded from multi-temperature 2D batch check.
- Trend consistency: expected-direction pass ratio 0.8125.

## Best GITT Held-Out Signals

- global / resistance_0p1s_ohm / r0_plus_voltage: MAE 0.000132, baseline MAE 0.001851, skill 0.929
- within_temperature / resistance_0p1s_ohm / r0_plus_voltage: MAE 0.0001744, baseline MAE 0.002057, skill 0.915
- within_temperature / resistance_0p1s_ohm / r0_only: MAE 0.0002611, baseline MAE 0.002057, skill 0.873
- global / resistance_0p1s_ohm / drt_plus_r0: MAE 0.0002526, baseline MAE 0.001851, skill 0.864
- global / resistance_0p1s_ohm / drt_plus_r0_voltage: MAE 0.0002663, baseline MAE 0.001851, skill 0.856
- global / resistance_0p1s_ohm / r0_only: MAE 0.000284, baseline MAE 0.001851, skill 0.847
- within_temperature / resistance_0p1s_ohm / voltage_only: MAE 0.0003748, baseline MAE 0.002057, skill 0.818
- within_temperature / c10_capacity_mah / voltage_only: MAE 50.94, baseline MAE 277.3, skill 0.816

## DRT Incremental Value

- DRT bands improved over R0 plus simple voltage features in 0 of 3 target/scope checks.
- global / soh: MAE delta -0.008738, skill delta -0.177, augmented better=False
- global / resistance_0p1s_ohm: MAE delta -0.0001343, skill delta -0.0726, augmented better=False
- global / c10_capacity_mah: MAE delta -56.83, skill delta -0.234, augmented better=False

## Locked R0 vs DRT Result

- R0 plus DRT bands beat R0 alone in 4 of 6 locked target/split checks.
- DRT bands without R0 had positive skill in 6 locked rows.
- leave_one_cell_out / resistance_0p1s_ohm / r0_only: MAE 0.000284, baseline MAE 0.001851, skill 0.847
- leave_one_cell_out / resistance_0p1s_ohm / r0_plus_drt_bands: MAE 0.0003306, baseline MAE 0.001851, skill 0.821
- leave_one_temperature_out / resistance_0p1s_ohm / r0_only: MAE 0.0003856, baseline MAE 0.001899, skill 0.797
- leave_one_temperature_out / resistance_0p1s_ohm / r0_plus_drt_bands: MAE 0.0004061, baseline MAE 0.001899, skill 0.786
- leave_one_cell_out / soh / r0_plus_drt_bands: MAE 0.02487, baseline MAE 0.04926, skill 0.495
- leave_one_cell_out / c10_capacity_mah / r0_plus_drt_bands: MAE 124.9, baseline MAE 242.9, skill 0.486
- leave_one_cell_out / c10_capacity_mah / drt_bands_only: MAE 140.5, baseline MAE 242.9, skill 0.421
- leave_one_cell_out / soh / drt_bands_only: MAE 0.02854, baseline MAE 0.04926, skill 0.421

## Best Multi-Protocol Held-Out Signals

- resistance_0p1s_ohm / all_protocols: MAE 0.0002813, baseline MAE 0.001851, skill 0.848
- c10_capacity_mah / gitt_only: MAE 39.42, baseline MAE 242.9, skill 0.838
- resistance_0p1s_ohm / gitt_only: MAE 0.0003902, baseline MAE 0.001851, skill 0.789
- soh / gitt_only: MAE 0.01127, baseline MAE 0.04926, skill 0.771
- soh / discharge_only: MAE 0.01151, baseline MAE 0.04947, skill 0.767
- c10_capacity_mah / discharge_only: MAE 58.13, baseline MAE 244.7, skill 0.762
- c10_capacity_mah / all_protocols: MAE 75.05, baseline MAE 244.7, skill 0.693
- resistance_0p1s_ohm / discharge_only: MAE 0.0005692, baseline MAE 0.001851, skill 0.693

## What Still Fails Scientifically

- No EIS-derived DRT comparison target was found in the inspected Expt4 folders.
- The strongest held-out result is mostly R0 predicting the 0.1s resistance label. Useful, but not surprising.
- Discharge capacity, capacity-normalized duration, capacity-axis voltage, and hybrid transition-count proxies are excluded for SOH/C10 strict checks. Good science sometimes means deleting your best-looking number.
- In the locked comparison, R0 plus DRT bands beat R0 alone in 4 of 6 checks. The gains are for SOH/C10, not resistance, and leave-one-temperature gains are small.
- The broader exploratory time-series 2D DRT surface DRT-over-R0-plus-voltage result is 0 of 3; treat it as secondary.
- Discharge and hybrid features help make the Zenodo package usable, but they are not DRT evidence.
- Temperature grouping can create fake-looking global structure. Within-temperature validation matters more.

## Done In This Run

- Fitted all accepted GITT pulses across the 25-pulse files: 1000 pulse fits.
- Aggregated GITT features by file and SOC/pulse-index proxy instead of relying on one selected pulse.
- Upgraded hybrid pulse segmentation: 17801 accepted hybrid segments.
- Kept the DRT physics claim blocked because no matched EIS source is attached to this Expt4 track.

## Do Next

1. Do not train a larger model yet. The DRT-band incremental signal is mixed and target-dependent.
2. Add matched EIS validation, probably through the DIB track, before claiming DRT physics.
3. Replace the ordered-pulse SOC proxy with measured or protocol-derived SOC if the source files expose it.
4. Diagnose why locked DRT bands help SOH/C10 but not the resistance target before expanding model complexity.

Blunt version: LG M50T 21700 Expt 4 drive-cycle aging is now a real multi-protocol health-feature scaffold. It is still not a substitute for the DIB EIS validation track.
