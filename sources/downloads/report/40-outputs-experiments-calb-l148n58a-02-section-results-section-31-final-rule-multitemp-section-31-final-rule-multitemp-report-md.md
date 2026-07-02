# CALB L148N58A, multi-temperature rule Final Rule Multi-Temperature Validation

## Purpose

Check whether the final record-aware bridge rule works across the CALB 10, 25, and 40 C fresh-cell grid.

## Result

- Row count: 246
- Quality-pass rows: 244
- Error count: 0
- Median quality-pass correlation: 0.9282125467314115
- Median quality-pass OCV delta: 0.003296648910522393 V
- Median quality-pass time RMSE: 3.1563794367812985 mV
- Verdict: `final_rule_multitemp_partial_pass`

## By Temperature

| Temperature | Rows | Pass rows | Median corr | Median OCV delta | Median RMSE |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 82 | 82 | 0.9281845691435505 | 0.003476104583740147 | 5.388854059089618 |
| 25 | 76 | 76 | 0.9285899403593834 | 0.00312132783508301 | 3.434061217973891 |
| 40 | 88 | 86 | 0.9279819711312928 | 0.0037321466674806736 | 2.629545900305935 |

## By Temperature And Record

| Temperature | Record | Rows | Pass rows | Median corr |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 0 | 22 | 22 | 0.9279890781196196 |
| 10 | 1 | 22 | 22 | 0.9284891933476155 |
| 10 | 2 | 22 | 22 | 0.9283595082110087 |
| 10 | 3 | 16 | 16 | 0.9256543962287673 |
| 25 | 0 | 22 | 22 | 0.9278122082483756 |
| 25 | 1 | 22 | 22 | 0.928817111728122 |
| 25 | 2 | 22 | 22 | 0.9287193640594177 |
| 25 | 3 | 10 | 10 | 0.928702463787356 |
| 40 | 0 | 22 | 22 | 0.9271029015604861 |
| 40 | 1 | 22 | 20 | 0.9287006267231805 |
| 40 | 2 | 22 | 22 | 0.9283208580161635 |
| 40 | 3 | 22 | 22 | 0.924964746278663 |

## Blunt Read

This is the overfitting check. If all temperatures pass, the final rule is much stronger than a 10 C rescue.

## Outputs

- `section_31_final_rule_rows.csv`
- `section_31_by_temperature.csv`
- `section_31_by_temperature_record.csv`
- `section_31_by_temperature_protocol.csv`
- `section_31_errors.csv`
- `section_31_summary.json`

## Linked Graph

![multi-temperature rule final rule multitemp](section_31_final_rule_multitemp.png)
