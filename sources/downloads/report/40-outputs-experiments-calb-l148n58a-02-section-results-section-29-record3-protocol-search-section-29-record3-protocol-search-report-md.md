# CALB L148N58A, record-3 protocol search Record-3 Protocol Search

## Purpose

Search every 10 C time-series protocol for a strict-comparable candidate for EIS record 3.

## Result

- Temperature tested: 10 C
- EIS record index: 3
- Protocols scanned: C20_Charge, C20_Discharge, DV_UDDS, DV_US06, DV_WLTP, HPPC_1C, HPPC_C3
- Candidate rows fitted: 144
- Error count: 0
- Skipped missing EIS-record cells: 3
- Best candidate: cell `60195`, protocol `HPPC_C3`, candidate `25`, OCV delta `0.0039887728576659676` V, RMSE `0.7905935624384443` mV, corr `0.9295091961482039`.
- Verdict: `record3_strict_candidate_found`

## By Protocol

| Protocol | Cell cases | Quality-pass cases | Median candidate OCV delta | Median RMSE | Median corr |
| --- | ---: | ---: | ---: | ---: | ---: |
| DV_UDDS | 8 | 0 | 0.028593292953491112 | 2.666626975589177 | 0.9261674246806707 |
| HPPC_1C | 8 | 8 | 0.007882655090332147 | 1.480559465265574 | 0.9248540709675204 |
| HPPC_C3 | 8 | 8 | 0.002621314285278231 | 0.8214103162490584 | 0.9261162519215498 |

## Coverage Summary

| Protocol | Cases | Raw voltage within 20 mV | Candidate within 20 mV | Median raw delta | Median candidate delta |
| --- | ---: | ---: | ---: | ---: | ---: |
| C20_Charge | 8 | 8 | 0 | 2.4357147216935715e-06 | None |
| C20_Discharge | 8 | 8 | 0 | 2.7685089112328143e-06 | None |
| DV_UDDS | 8 | 8 | 0 | 5.468139648412418e-06 | 0.028593292953491112 |
| DV_US06 | 8 | 8 | 0 | 1.7314910889520974e-06 | None |
| DV_WLTP | 8 | 8 | 0 | 7.603149414503463e-07 | None |
| HPPC_1C | 8 | 8 | 8 | 3.5612487794267622e-06 | 0.007882655090332147 |
| HPPC_C3 | 8 | 8 | 8 | 2.886047363315214e-07 | 0.0016240642852782816 |

## Blunt Read

Record 3 is solved only if a same-cell protocol has a candidate inside the OCV gate, a voltage fit inside the RMSE gate, and high gamma correlation.
High correlation with a 70 to 150 mV OCV mismatch is not a same-state bridge.

## Outputs

- `section_29_candidate_rows.csv`
- `section_29_protocol_summary.csv`
- `section_29_coverage_rows.csv`
- `section_29_coverage_summary.csv`
- `section_29_skipped_rows.csv`
- `section_29_errors.csv`
- `section_29_summary.json`

## Linked Graph

![record-3 protocol search record3 protocol search](section_29_record3_protocol_search.png)
