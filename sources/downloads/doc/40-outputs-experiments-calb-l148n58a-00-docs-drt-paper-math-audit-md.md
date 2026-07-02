# CALB DRT Paper Math Audit

## Source

- Paper: Wildfeuer, Gieler, and Karger, `Combining the Distribution of Relaxation Times from EIS and Time-Domain Data for Parameterizing Equivalent Circuit Models of Lithium-Ion Batteries`, Batteries 2021, 7(3), 52.
- DOI: https://doi.org/10.3390/batteries7030052
- Local PDF checked: not recorded in the repository; set `CALB_DRT_PAPER_PDF` locally if needed.

## Verdict

The paper supports the direction of this project, but it also exposes the current weak spot.

Our current time-domain pipeline fits a DRT-like gamma curve from voltage/current windows, then compares against EIS after the fit. The paper's strongest method instead builds one combined inverse problem where EIS and time-domain pulse relaxation constrain the same DRT at the same time.

Blunt version: CALB gives us the data to attempt the better method. If we stop at post-hoc EIS comparison, we are leaving the strongest math on the table.

## What Matches

- Both approaches model polarization as a distribution of RC relaxation processes over log tau.
- Both use nonnegative resistance weights because negative resistance is not physically defensible.
- Both need Tikhonov-style regularization because DRT inversion is ill-posed.
- Both treat tau-grid choice as a real modeling decision, not a cosmetic setting.
- Both warn, implicitly or directly, that voltage reconstruction alone does not prove the recovered DRT is physically right.

## What Does Not Match Yet

- The paper uses an L-curve rule for regularization selection. Our existing pipeline uses a pre-declared model rule and lambda grid, which is honest but not the same criterion.
- The paper derives EIS-DRT from real and imaginary impedance together. The CALB package has `frequency_hz`, `zreal_ohm`, and `zimg_ohm`, but this first pass has not solved EIS-DRT yet.
- The paper's combined DRT fitting merges EIS and pulse-relaxation residuals into one objective. Our current solver does time-domain first and compares EIS later.
- The paper parameterizes ECM RC elements from DRT peaks and adjacent minima. Our package currently reports gamma bands and peaks as diagnostics, not final ECM parameters.
- The paper is careful about OCV and long relaxation before pulse measurements. CALB drive cycles are richer and messier, so blindly applying the paper's pulse-relaxation assumptions to WLTP/UDDS/US06 would be sloppy.

## CALB Fit To The Paper

- Cells available in processed data: 11.
- Temperatures: 10 C, 25 C, 40 C.
- Protocols: C20_Charge, C20_Discharge, DV_UDDS, DV_US06, DV_WLTP, EIS_test, HPPC_1C, HPPC_C3.
- EIS is present for the same cell and temperature as the first slice.
- HPPC and low-rate C/20 protocols are present and are better first choices for pulse-relaxation fitting than full drive cycles.
- Drive cycles are still useful for validation after parameterization, especially because the paper validates on dynamic current profiles.

## First Slice Evidence

- Cell: `59294`.
- Temperature: `25 C`.
- `DV_WLTP`: 221,437 rows, 7.50 h, current -60.08 to 19.42 A, median dt 0.1 s.
- `DV_UDDS`: 239,440 rows, 8.00 h, current -59.38 to 36.17 A, median dt 0.1 s.
- `DV_US06`: 119,243 rows, 4.66 h, current -59.99 to 26.99 A, median dt 0.1 s.
- `HPPC_1C`: 172,269 rows, 12.43 h, current -58.00 to 37.70 A, median dt 0.1001 s.
- `HPPC_C3`: 172,850 rows, 12.45 h, current -58.01 to 37.70 A, median dt 0.1001 s.
- `EIS_test`: 120 rows, 3 OCV records, 0.01 to 3722 Hz.

## Recommended Next Implementation

1. Build an EIS-DRT solver for CALB `EIS_test.csv` using real and imaginary impedance together.
2. Build a pulse-relaxation TDM-DRT fit on `HPPC_1C.csv` or `HPPC_C3.csv`, not on a whole drive cycle first.
3. Add L-curve diagnostics beside the existing lambda-grid rule.
4. Implement combined fitting where EIS and TDM residuals share one gamma vector.
5. Only after the combined method works, validate voltage prediction on `DV_WLTP.csv`, `DV_UDDS.csv`, and `DV_US06.csv`.

## Professor-Safe Claim

A defensible claim right now: `CALB has the same measurement ingredients needed for a combined EIS plus time-domain DRT validation experiment, and the first slice confirms same-cell, same-temperature drive-cycle, HPPC, C/20, and EIS files are readable.`

Do not claim: `We have validated the combined DRT method on CALB.` That would be false today.
