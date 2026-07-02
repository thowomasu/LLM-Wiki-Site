# Panasonic 18650PF Frozen frozen pulse-to-EIS rule Adapter Run

## Verdict

`no support`

## What Was Run

The adapter discovered Panasonic rows with the same cell ID in `dis5_10p` pulse files and EIS CSV files, then fed those rows into the unchanged CALB frozen pulse-to-EIS rule adaptive final rule helper.

No lambda, candidate rule, window length, fallback rule, or pass criterion was tuned on Panasonic data.

## Counts

- Adapter join rows: 3
- Frozen rule rows: 33
- Quality-pass rows: 0
- Error rows: 2
- Voltage-only baseline pass rows: 14

## Blunt Read

Panasonic is runnable as an adapter smoke test, but this run does not support the frozen frozen pulse-to-EIS rule claim. The rule does not beat the boring voltage-only baseline on the current mapped rows.

This is also not aging validation. It is a different-cell-format pulse-to-EIS bridge check.

## Outputs

- `panasonic_adapter_candidate_table.csv`
- `panasonic_frozen_rule_rows.csv`
- `panasonic_by_temperature.csv`
- `panasonic_by_temperature_record.csv`
- `panasonic_by_temperature_protocol.csv`
- `panasonic_frozen_rule_errors.csv`
- `panasonic_frozen_rule_summary.json`
