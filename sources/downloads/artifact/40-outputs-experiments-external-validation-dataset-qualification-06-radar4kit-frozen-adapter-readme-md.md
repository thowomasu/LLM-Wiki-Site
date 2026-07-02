# RADAR4KIT Frozen frozen pulse-to-EIS rule Adapter Run

## Verdict

`no support`

## What Was Run

Corrected RADAR4KIT EIS rows were joined to `cell_plsv2` pulse rows by the shared file key and `soc_nom`, then fed into the unchanged CALB frozen pulse-to-EIS rule adaptive final rule helper.

No lambda, candidate rule, window length, fallback rule, or pass criterion was tuned on RADAR4KIT data.

## Counts

- Adapter join rows: 228
- Frozen rule rows: 456
- Quality-pass rows: 411
- Error rows: 684
- Voltage-only baseline pass rows: 454

## Blunt Read

This adapter check is useful, but it is not a drive-cycle or aging validation result. If the frozen CALB record-specific candidate rule does not transfer, that is a real limitation.

## Outputs

- `radar4kit_adapter_candidate_table.csv`
- `radar4kit_frozen_rule_rows.csv`
- `radar4kit_by_temperature.csv`
- `radar4kit_by_temperature_record.csv`
- `radar4kit_by_temperature_protocol.csv`
- `radar4kit_frozen_rule_errors.csv`
- `radar4kit_frozen_rule_summary.json`
