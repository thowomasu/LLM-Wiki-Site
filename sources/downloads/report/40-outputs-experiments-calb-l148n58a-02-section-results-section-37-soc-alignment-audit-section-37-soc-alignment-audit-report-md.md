# CALB L148N58A, SOC alignment audit SOC Alignment Audit

## Purpose

Use same-cell, same-temperature C/20 discharge curves as a rough protocol-aware voltage-to-SOC reference for the final bridge and drive-cycle rows.

## Result

- C/20 curves loaded: 33
- Bridge rows audited: 246
- Drive rows audited: 198
- Error count: 0
- Median bridge abs SOC delta: 0.004556003613014614
- 95th percentile bridge abs SOC delta: 0.010119652664487264
- Bridge rows above 2 percent SOC delta: 0
- Bridge rows above 5 percent SOC delta: 0
- Median drive-to-EIS abs SOC delta: 0.0637559086707088
- 95th percentile drive-to-EIS abs SOC delta: 0.10274714623982303
- Drive rows above 5 percent SOC delta: 182
- Drive rows above 10 percent SOC delta: 40
- Verdict: `soc_alignment_audit_complete`

## Blunt Read

This is a better alignment audit than raw OCV delta, but it is not a full SOC estimator. Hysteresis, rest history, and charge/discharge path still matter. Treat large SOC deltas as real warnings, not proof of failure.

## Outputs

- `section_37_bridge_soc_alignment_rows.csv`
- `section_37_drive_soc_alignment_rows.csv`
- `section_37_c20_curve_summary.csv`
- `section_37_errors.csv`
- `section_37_summary.json`

## Linked Graph

![SOC alignment audit soc alignment audit](section_37_soc_alignment_audit.png)
