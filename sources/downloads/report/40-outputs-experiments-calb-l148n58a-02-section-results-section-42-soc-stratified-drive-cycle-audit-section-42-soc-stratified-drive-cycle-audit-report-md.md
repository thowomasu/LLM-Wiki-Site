# CALB L148N58A, SOC-stratified drive-cycle audit SOC-Stratified Drive-Cycle Audit

## Purpose

Check whether the drive-cycle result improves when the drive-cycle ECM baseline check stronger ECM comparison is stratified by SOC alignment audit SOC alignment.

## Result

- Rows: 198
- Rows within 5 percent SOC delta: 16
- Rows above 5 percent SOC delta: 182
- Aligned DRT win fraction vs best ECM: 0.0
- Misaligned DRT win fraction vs best ECM: 0.13186813186813187
- Verdict: `drive_cycle_result_soc_misaligned_and_ecm_baseline_still_stronger`

## Blunt Read

There are too few SOC-aligned drive-cycle rows to rescue the transfer claim. The honest conclusion is not `DRT wins after stratification`; it is `the drive-cycle test needs a cleaner state-aligned design`.

## Outputs

- `section_42_soc_stratified_rows.csv`
- `section_42_by_soc_bucket.csv`
- `section_42_by_soc_bucket_protocol_temperature.csv`
- `section_42_summary.json`
