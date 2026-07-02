# CALCE Storage 25 C Frozen Rule Run

## Verdict

`blocked/inconclusive`

## What Happened

The frozen frozen pulse-to-EIS rule was not run on CALCE.

Reason: the current CALCE frozen inputs expose same-PLN capacity and impedance qualification evidence, but they do not expose HPPC-compatible pulse windows required by the frozen pulse-to-EIS rule candidate selector and time-domain fit.

No lambda, threshold, time window, candidate rule, fallback rule, or pass criterion was changed.

## Counts

- Frozen input rows: 24
- Runnable rows: 0
- Blocked rows: 24

## Claim Boundary

This is blocked external validation readiness, not external support.

frozen pulse-to-EIS rule remains internal CALB pulse-bridge evidence only.

## Outputs

- `calce_storage_25c_frozen_rule_blockers.csv`
- `calce_storage_25c_frozen_rule_summary.json`
- `README.md`
