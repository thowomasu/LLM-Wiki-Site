# CALB L148N58A, final 10 C rule Final 10 C Pipeline

## Purpose

Run the final unified 10 C bridge rule discovered in cold EIS-window probe through record-3 protocol search.

## Result

- Row count: 82
- Quality-pass rows: 82
- Error count: 0
- Median quality-pass correlation: 0.9281845691435505
- Median quality-pass OCV delta: 0.003476104583740147 V
- Median quality-pass time RMSE: 5.388854059089618 mV
- Verdict: `final_10c_all_rows_pass`

## By Record

| Record | Rows | Pass rows | Median corr | Median OCV delta | Median RMSE |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 22 | 22 | 0.9279890781196196 | 0.0032164999999997335 | 5.805427228230771 |
| 1 | 22 | 22 | 0.9284891933476155 | 0.003590250000000017 | 4.9694844242360645 |
| 2 | 22 | 22 | 0.9283595082110087 | 0.002227500000000049 | 5.9582611940582355 |
| 3 | 16 | 16 | 0.9256543962287673 | 0.004359372055053656 | 1.1207732383423592 |

## By Protocol

| Protocol | Rows | Pass rows | Median corr | Median OCV delta | Median RMSE |
| --- | ---: | ---: | ---: | ---: | ---: |
| HPPC_1C | 41 | 41 | 0.928120851373666 | 0.005308360412597857 | 5.397235155248199 |
| HPPC_C3 | 41 | 41 | 0.9282648777018252 | 0.001017078155517659 | 5.380472962931036 |

## Candidate Rule

- Records 0 to 2: nearest long HPPC discharge candidate.
- Record 3: nearest accepted short HPPC candidate.
- EIS target: 0.03 to 50 Hz, lambda 3.
- Time-domain fit: tau constrained to EIS support, `time_charge` baseline, 120 s pre-window, 1200 s post-window.

## Blunt Read

The 10 C bridge now has one reproducible rule. The previous record-3 failure was caused by the long-pulse candidate filter, not by missing EIS/time-domain agreement.

## Outputs

- `section_30_final_10c_rows.csv`
- `section_30_by_record.csv`
- `section_30_by_protocol.csv`
- `section_30_by_record_protocol.csv`
- `section_30_errors.csv`
- `section_30_summary.json`

## Linked Graph

![final 10 C rule final 10c pipeline](section_30_final_10c_pipeline.png)
