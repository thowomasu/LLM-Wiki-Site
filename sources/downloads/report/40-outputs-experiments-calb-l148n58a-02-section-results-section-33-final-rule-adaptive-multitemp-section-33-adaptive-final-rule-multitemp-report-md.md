# CALB L148N58A, frozen pulse-to-EIS rule Final Rule Adaptive Multi-Temperature Validation

## Purpose

Validate the final bridge rule across 10, 25, and 40 C with a narrow EIS regularization fallback for correlation-only failures.

## Result

- Row count: 246
- Quality-pass rows: 246
- Error count: 0
- Fallback rows: 2
- Median quality-pass correlation: 0.928192585051496
- Median quality-pass OCV delta: 0.003296648910522393 V
- Median quality-pass time RMSE: 3.144651471038199 mV
- EIS lambda sequence: `[3.0, 0.1]`
- Verdict: `adaptive_final_rule_all_temperatures_all_rows_pass`

## By Temperature

| Temperature | Rows | Pass rows | Median corr | Median OCV delta | Median RMSE |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 82 | 82 | 0.9281845691435505 | 0.003476104583740147 | 5.388854059089618 |
| 25 | 76 | 76 | 0.9285899403593834 | 0.00312132783508301 | 3.434061217973891 |
| 40 | 88 | 88 | 0.9279569777620462 | 0.0037321466674806736 | 2.6285800912655777 |

## Fallback Rows

| Temperature | Cell | Protocol | Record | Candidate | Lambda | Corr | OCV delta | RMSE |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 40 | 59861 | HPPC_1C | 1 | 15 | 0.1 | 0.9161807404837676 | 0.005558648223876972 | 2.407601120346446 |
| 40 | 59861 | HPPC_C3 | 1 | 15 | 0.1 | 0.9161807404931611 | 0.0023213517761231373 | 2.3793611789777844 |

## Blunt Read

This is no longer a 10 C-only solution. The only added flexibility is an EIS regularization retry for rows that already pass OCV and time-domain RMSE. That is defensible. A broader candidate search would be weaker evidence.

## Outputs

- `section_33_adaptive_final_rule_rows.csv`
- `section_33_by_temperature.csv`
- `section_33_by_temperature_record.csv`
- `section_33_by_temperature_protocol.csv`
- `section_33_fallback_rows.csv`
- `section_33_errors.csv`
- `section_33_summary.json`

## Linked Graph

![frozen pulse-to-EIS rule adaptive final rule](section_33_adaptive_final_rule_multitemp.png)
