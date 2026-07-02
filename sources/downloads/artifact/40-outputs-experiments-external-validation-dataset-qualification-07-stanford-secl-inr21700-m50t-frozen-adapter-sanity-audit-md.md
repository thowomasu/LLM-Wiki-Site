# Stanford SECL Adapter Sanity Audit

## Verdict

`adapter_sane_result_no_support`

## Checks

- Complete SOC20/50/80 joins: 61 of 61
- Raw sampled joins: 12
- OCV monotonic SOC80 > SOC50 > SOC20 in fitted rows: True
- OCV monotonic in sampled raw joins: True
- Long-discharge candidates present in sampled raw joins: True
- README phase unit: degrees
- Adapter phase conversion expected: True
- Minimum EIS fit-band points: 10
- Median EIS channel voltage span: 0.013641119003295898 V

## Frozen-Run Result

- Fitted rows: 182
- Quality-pass rows: 0
- Voltage-only baseline-pass rows: 76
- Max correlation: 0.7176841605422476

## Blunt Read

The adapter mapping looks sane. The failed result should not be blamed on the Dropbox download, missing cycling data, or an obvious phase-unit/parser mistake.

This does not validate the frozen CALB rule. It makes the negative external result harder to dismiss.
