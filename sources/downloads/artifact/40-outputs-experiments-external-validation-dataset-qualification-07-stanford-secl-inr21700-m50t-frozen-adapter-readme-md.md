# Stanford SECL INR21700-M50T Frozen frozen pulse-to-EIS rule Adapter Run

## Verdict

`no support`

## What Was Run

SECL diagnostic HPPC files were joined to EIS files by diagnostic round, cell label, channel, and SOC. SOC80, SOC50, and SOC20 were mapped to frozen pulse-to-EIS rule record indices 0, 1, and 2.

No lambda, candidate rule, window length, fallback rule, or pass criterion was tuned on SECL data.

## Counts

- Adapter join rows: 61
- Frozen rule rows: 182
- Quality-pass rows: 0
- Error rows: 1
- Voltage-only baseline pass rows: 76

## Blunt Read

This is a real external adapter check because it has same-cell HPPC and EIS. It is still not drive-cycle or SOH validation, and it only supports the frozen claim if it beats the voltage-only baseline.

## Outputs

- `stanford_secl_adapter_candidate_table.csv`
- `stanford_secl_frozen_rule_rows.csv`
- `stanford_secl_by_temperature.csv`
- `stanford_secl_by_temperature_record.csv`
- `stanford_secl_by_temperature_protocol.csv`
- `stanford_secl_frozen_rule_errors.csv`
- `stanford_secl_frozen_rule_summary.json`
