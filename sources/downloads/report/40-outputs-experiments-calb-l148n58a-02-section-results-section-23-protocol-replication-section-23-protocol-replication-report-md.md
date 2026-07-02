# CALB L148N58A, protocol replication check Protocol Replication

## Purpose

Replicate the tau-constrained pulse-to-EIS fit EIS-tau-constrained HPPC bridge on both HPPC_1C and HPPC_C3.

## Result

- Rows: 246
- Quality-pass rows: 203
- Error count: 0
- Median default correlation: -0.048314053447822185
- Median constrained correlation: 0.8924652435154302
- Median constrained-minus-default correlation: 0.6965678707428696
- Viability label: `pulse_bridge_viable`

## By Protocol

| Protocol | Rows | Quality-pass | Default corr | Constrained corr | Delta | Better rows | RMSE mV | Abs OCV delta mV |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| HPPC_1C | 123 | 99 | -0.0485998081564577 | 0.8956430786264292 | 0.6464111745046026 | 97 | 2.654828741254241 | 4.673578582763849 |
| HPPC_C3 | 123 | 104 | -0.04808220473514489 | 0.8889282185609136 | 0.7289229905347203 | 103 | 2.7993990718156834 | 1.7669241638185174 |

## By Temperature And Protocol

| Temperature C | Protocol | Rows | Quality-pass | Constrained corr | Delta |
| ---: | --- | ---: | ---: | ---: | ---: |
| 10 | HPPC_1C | 41 | 33 | -0.024759216494058073 | 0.032086527551436775 |
| 10 | HPPC_C3 | 41 | 33 | -0.025730164828398367 | 0.029521095316102006 |
| 25 | HPPC_1C | 38 | 33 | 0.8967712661000141 | 0.14106962805479017 |
| 25 | HPPC_C3 | 38 | 33 | 0.8956991868492752 | 0.13035834121019726 |
| 40 | HPPC_1C | 44 | 33 | 0.9083556858084912 | 0.9633146586579924 |
| 40 | HPPC_C3 | 44 | 38 | 0.9068843982253243 | 0.9555897070798802 |

## Blunt Read

If HPPC_C3 tracks HPPC_1C, the tau-constrained bridge is viable for CALB pulse-test DRT comparison.
If HPPC_C3 collapses, tau-constrained pulse-to-EIS fit was a protocol-specific result and should not be presented as a general pipeline.

## Outputs

- `section_23_protocol_replication_rows.csv`
- `section_23_by_protocol.csv`
- `section_23_by_temperature_protocol.csv`
- `section_23_errors.csv`
- `section_23_summary.json`

## Linked Graph

![protocol replication check protocol replication](section_23_protocol_replication.png)
