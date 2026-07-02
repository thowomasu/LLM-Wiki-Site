# CALCE Storage 25 C Frozen Inputs

## Scope

This folder freezes the CALCE qualification rows for external validation planning. It is not an external validation result.

Rows are included only when the adapter exposes same-PLN, same-temperature, same-storage-period, and same-SOC evidence. Blockers and dirty joins are reported at row level instead of patched.

## Result

- Row count: 24
- Same-join justified rows: 24
- Dirty-join warning rows: 24
- frozen pulse-to-EIS rule runnable rows: 0
- Blocked rows: 24
- Verdict: `blocked_no_hppc_compatible_pulse_windows`

## Blunt Read

CALCE is still the right first external target, but the current adapter output does not expose HPPC-compatible pulse windows. Capacity workbook summaries plus EIS spectra are not enough to run frozen pulse-to-EIS rule honestly.

The weak spot is multiplicity. Some CALCE storage-period rows have multiple capacity and impedance matches under one PLN-period condition. That is not fatal for qualification, but it blocks a clean single-row validation claim until the timepoint mapping is made explicit.

## Outputs

- `calce_storage_25c_frozen_input_rows.csv`
- `calce_storage_25c_frozen_input_summary.json`
- `README.md`
