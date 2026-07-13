# Professor Brief

## Bottom Line

LG M50T 21700 Expt 4 drive-cycle aging is now defensible as a multi-protocol internal health-feature benchmark.
It is not defensible as EIS-validated DRT physics.
The strongest honest claim is that GITT-derived R0 and broad DRT-band summaries carry same-dataset health signal, with R0 dominating resistance prediction and DRT bands adding mixed SOH/C10 signal.

## What Improved

- Full GITT batch now fits all accepted pulses: 1000 pulse fits across 40 files.
- Discharge validation now has fixed-time voltage features, so SOH/C10 checks do not rely on capacity-axis voltage points.
- multi-temperature 2D batch check now excludes 64 target-proxy feature uses.
- combined DRT mirror check adds the locked comparison: R0 only, DRT bands only, and R0 plus DRT bands.
- Trend consistency remains above the rough pass line: 0.812 expected-direction pass ratio.

## Best Results

Locked GITT-only comparison:
- leave_one_cell_out / resistance_0p1s_ohm / r0_only: MAE 0.000284, baseline MAE 0.001851, skill 0.847
- leave_one_cell_out / resistance_0p1s_ohm / r0_plus_drt_bands: MAE 0.0003306, baseline MAE 0.001851, skill 0.821
- leave_one_temperature_out / resistance_0p1s_ohm / r0_only: MAE 0.0003856, baseline MAE 0.001899, skill 0.797
- leave_one_temperature_out / resistance_0p1s_ohm / r0_plus_drt_bands: MAE 0.0004061, baseline MAE 0.001899, skill 0.786
- leave_one_cell_out / soh / r0_plus_drt_bands: MAE 0.02487, baseline MAE 0.04926, skill 0.495
- leave_one_cell_out / c10_capacity_mah / r0_plus_drt_bands: MAE 124.9, baseline MAE 242.9, skill 0.486

Strict multi-protocol comparison:
- resistance_0p1s_ohm / all_protocols: MAE 0.0002813, baseline MAE 0.001851, skill 0.848
- c10_capacity_mah / gitt_only: MAE 39.42, baseline MAE 242.9, skill 0.838
- resistance_0p1s_ohm / gitt_only: MAE 0.0003902, baseline MAE 0.001851, skill 0.789
- soh / gitt_only: MAE 0.01127, baseline MAE 0.04926, skill 0.771
- soh / discharge_only: MAE 0.01151, baseline MAE 0.04947, skill 0.767
- c10_capacity_mah / discharge_only: MAE 58.13, baseline MAE 244.7, skill 0.762

## What Still Fails

- No paired EIS-derived DRT target exists in the inspected Expt4 package.
- DRT bands do not improve resistance prediction over R0. R0 is the resistance feature.
- The DRT-band gain for SOH/C10 is internal and target-dependent, not physical validation.
- Leave-one-temperature-out gains are smaller than leave-one-cell-out gains, so temperature and protocol context still matter.
- Hybrid features remain exploratory. They are useful health summaries, not DRT evidence.

## What You Cannot Claim

- Do not claim EIS validation.
- Do not claim recovered gamma peaks are validated electrochemical processes.
- Do not claim hybrid-only results prove independent SOH inference.
- Do not claim the all-protocol score proves DRT adds major value.

## Roadmap

1. Add matched EIS or EIS-derived DRT on the same cells and RPT points.
2. Replace ordered-pulse SOC buckets with measured or protocol-confirmed SOC annotations.
3. Stress-test the locked feature comparison on another dataset before adding model complexity.
4. Keep R0, DRT bands without R0, and R0 plus DRT bands as the locked baseline trio.

Blunt script for the meeting: this is a solid health-feature benchmark now, not a validated DRT physics result.
