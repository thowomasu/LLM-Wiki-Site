# CALCE Storage 25 C Validation Report

## Verdict

`blocked/inconclusive`

## What This Supports

CALCE Storage 25 C supports external validation readiness work because the current adapter can freeze same-PLN, same-temperature, same-storage-period, and same-SOC qualification rows.

It does not externally validate the CALB frozen pulse-to-EIS rule.

## What Blocks Validation

- The current CALCE frozen inputs do not expose HPPC-compatible pulse windows.
- Capacity summaries and EIS spectra are not enough to run the frozen pulse-to-EIS rule pulse-bridge rule.
- A fair baseline comparison is still unavailable because the frozen rule did not run.
- Dirty join multiplicity remains visible in the row-level frozen input table.

## Counts

- Frozen input rows: 24
- Same-join justified rows: 24
- frozen pulse-to-EIS rule runnable rows: 0
- Frozen rule run attempted: False
- Baseline run attempted: False

## Claim Boundary

frozen pulse-to-EIS rule remains internal CALB pulse-bridge evidence only. This CALCE report is blocked/inconclusive external validation readiness, not external support.

## Next Requirement

Find or build a CALCE path that exposes same-PLN HPPC-compatible pulse windows tied to the same 25 C, storage-period, and SOC rows. Without that, using frozen pulse-to-EIS rule here would be pretending.

## Outputs

- `calce_storage_25c_validation_summary.json`
- `README.md`
