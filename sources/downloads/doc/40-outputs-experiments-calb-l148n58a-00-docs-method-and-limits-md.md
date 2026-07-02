# CALB Method And Limits

## What Is Implemented

- HPPC window discovery on the first slice.
- Time-domain DRT fitting on one selected HPPC window.
- EIS DRT baseline using real plus imaginary impedance in one NNLS problem.
- Post-hoc time-domain versus EIS comparison.
- Lambda and L-curve-style diagnostics.
- A rough combined EIS plus time-domain DRT prototype.
- Time-series 2D DRT surface from long HPPC discharge pulses.
- EIS 2D DRT surface from same-cell, same-temperature EIS records.
- Same-dataset 2D DRT comparison harness.
- 25 C multi-cell 2D comparison across all 11 processed cells.
- Multi-temperature 2D comparison across 10, 25, and 40 C.
- Tau-constrained HPPC bridge replication across HPPC_1C and HPPC_C3.
- 10 C cold-temperature diagnosis across every long HPPC candidate in both pulse protocols.
- 10 C strict-match EIS and time-domain regularization sweeps.
- Final 10 C record-aware bridge pipeline, 82 of 82 rows pass.
- Final adaptive multi-temperature bridge validation across 10, 25, and 40 C, 246 of 246 rows pass with 2 narrow EIS-lambda fallback rows.
- Drive-cycle voltage holdout validation using fixed HPPC-derived DRT dynamics from the frozen pulse-to-EIS rule bridge rows.
- Stronger drive-cycle ECM-style baseline audit against the fixed frozen pulse-to-EIS rule/34 DRT transfer result.
- C/20-derived SOC/protocol alignment audit for the frozen pulse-to-EIS rule bridge rows and drive-cycle transfer test/36 drive-cycle calibration rows.
- Bootstrap uncertainty audit across the final bridge, drive-cycle baseline, and SOC-alignment metrics.
- External replication readiness audit across the local KIT/RADAR4KIT, Zenodo Expt4, and DIB comparison evidence.

## What Is Not Proven

- SOH or aging prediction. CALB is fresh-cell characterization.
- Exact SOC matching between every protocol pair. SOC alignment audit supports tight SOC alignment for the pulse bridge, but not for the drive-cycle calibration rows.
- Validated combined DRT method. combined EIS and time-domain DRT prototype only proves a prototype runs.
- Time-domain gamma agreement with EIS gamma. multi-cell 2D batch check and multi-temperature 2D batch check show tight OCV matching but weak median shape correlation.
- Drive-cycle voltage prediction is internally tested in drive-cycle transfer test and drive-cycle ECM baseline check, but fixed HPPC-derived DRT loses to the stronger drive-cycle ECM baseline check drive-cycle-fitted ECM baseline.
- External dataset generalization.
- External replication readiness. external-validation claim boundary says the current local evidence is blocked by missing or insufficient EIS pairing.
- A broad lambda-tuning fix. frozen pulse-to-EIS rule uses a narrow fallback only for correlation-only failures after OCV and time RMSE already pass.

## Blunt Next Move

frozen pulse-to-EIS rule is the current defensible CALB bridge result: 246 of 246 rows pass across the fresh-cell temperature grid.
Do not inflate that into a battery-health claim. drive-cycle transfer test adds a positive first drive-cycle transfer test against baseline-only drift. drive-cycle ECM baseline check adds the stronger internal ECM-baseline audit and fixed DRT loses. SOC alignment audit shows the pulse bridge is SOC-aligned, while the drive-cycle transfer is not. analysis step 38 says those two conclusions are stable under bootstrap resampling. external-validation claim boundary says external replication is blocked until the corrected KIT/RADAR4KIT EIS addendum or another same-cell EIS-paired dataset is available. The next real proof step is corrected external EIS plus a SOC-aligned drive-cycle rerun, not another internal rescue plot.
Keep multi-temperature 2D batch check separate from frozen pulse-to-EIS rule: the older 2D comparison is a harness with weak gamma-shape agreement, while the final tau-constrained bridge is the solved result.

drive-cycle transfer test drive-cycle note: drive-cycle transfer test drive-cycle validation: 198 rows; DRT win fraction 1.0; median DRT holdout RMSE 150.9172295922953 mV, median baseline holdout RMSE 164.95303653565315 mV; verdict `drive_cycle_transfer_supports_hppc_drt`.

drive-cycle ECM baseline check ECM-baseline note: drive-cycle ECM baseline check stronger drive-cycle ECM baseline audit: 198 rows; median fixed DRT RMSE 150.9172295922953 mV, median best ECM RMSE 134.8626012268972 mV, DRT win fraction 0.12121212121212122; verdict `drive_cycle_ecm_baseline_beats_fixed_drt`.

SOC alignment audit SOC-alignment note: bridge median absolute SOC delta 0.004556003613014614 with zero rows above 2 percent SOC delta; drive-cycle median absolute SOC delta 0.0637559086707088 with 182 of 198 rows above 5 percent SOC delta; verdict `soc_alignment_audit_complete`.

analysis step 38 uncertainty note: 12 metrics bootstrapped with 5000 samples; the drive-cycle ECM baseline check DRT loss to best ECM and the SOC alignment audit drive-cycle SOC mismatch remain stable under row resampling; verdict `uncertainty_audit_complete`.

external-validation claim boundary external-readiness note: three hard blockers remain, including incomplete local KIT EIS archive, no same-cell EIS in local Zenodo Expt4 evidence, and too-small DIB overlap; verdict `external_replication_blocked_missing_corrected_eis`.



leakage and claim audit-42 local-audit note: leakage and claim audit marks the final CALB rule as internally engineered, not clean held-out validation; analysis step 41 consolidates the local ablations; SOC-stratified drive-cycle audit shows only 16 of 198 drive-cycle rows are within 5 percent SOC delta. This reinforces the next step: corrected external EIS plus SOC-clean drive-cycle validation.
