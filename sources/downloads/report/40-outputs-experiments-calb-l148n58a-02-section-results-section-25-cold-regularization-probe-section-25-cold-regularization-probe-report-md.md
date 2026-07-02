# CALB L148N58A, cold regularization probe Cold Regularization Probe

## Purpose

Test whether the 10 C strict-match failure is fixed by changing EIS-side or time-domain regularization.

## Result

- Temperature tested: 10 C
- Protocols: HPPC_1C, HPPC_C3
- Cells attempted per protocol: 11
- EIS lambda rows: 656
- Time lambda rows: 492
- Error count: 0
- Best EIS lambda summary: `{'eis_lambda': 30.0, 'median_corr_quality': 0.39841347979707287, 'corr_ge_0p75_rows_quality': 0, 'median_scaled_rmse_quality': 0.9052378439001971}`
- Best time lambda summary: `{'time_lambda': 1e-05, 'median_corr_quality': -0.024996621276100403, 'corr_ge_0p75_rows_quality': 26, 'median_scaled_rmse_quality': 0.9999992553806383}`

## EIS Lambda Summary

| EIS lambda | Quality-pass | Median corr | Corr >= 0.75 rows | Median scaled RMSE |
| ---: | ---: | ---: | ---: | ---: |
| 0.0001 | 66 | -0.024996672231838945 | 26 | 0.9999992558893714 |
| 0.001 | 66 | -0.024996672226797703 | 26 | 0.9999992558893209 |
| 0.01 | 66 | -0.02499667172269463 | 26 | 0.9999992558842843 |
| 0.1 | 66 | -0.024996621549416252 | 26 | 0.9999992553806807 |
| 1.0 | 66 | -0.024960116528054046 | 26 | 0.9999992488192013 |
| 3.0 | 66 | 0.04776138324719853 | 26 | 0.9966293626396826 |
| 10.0 | 66 | 0.25249620088820796 | 21 | 0.9580592808276096 |
| 30.0 | 66 | 0.39841347979707287 | 0 | 0.9052378439001971 |

## Time Lambda Summary

| Time lambda | Quality-pass | Median corr | Corr >= 0.75 rows | Median time RMSE mV |
| ---: | ---: | ---: | ---: | ---: |
| 1e-05 | 66 | -0.024996621276100403 | 26 | 3.946746230760313 |
| 0.0001 | 66 | -0.02499662127880671 | 26 | 3.9467462307603096 |
| 0.001 | 66 | -0.024996621549416252 | 26 | 3.9467462307603114 |
| 0.01 | 66 | -0.024996648609863375 | 26 | 3.946746230760316 |
| 0.1 | 66 | -0.024999350258903458 | 26 | 3.9467462308164514 |
| 1.0 | 66 | -0.025056307062538412 | 26 | 3.9467463642192007 |

## Blunt Read

Time-domain lambda does not move the 10 C result in any meaningful way.
Heavy EIS smoothing can raise the aggregate median, but record 0 remains negative and record 2 gets worse. That is not a clean fix.
The next honest work is model-form or cold-specific EIS/OCV treatment, not another lambda sweep.

## Outputs

- `section_25_eis_lambda_rows.csv`
- `section_25_time_lambda_rows.csv`
- `section_25_by_eis_lambda.csv`
- `section_25_by_time_lambda.csv`
- `section_25_by_record_eis_lambda.csv`
- `section_25_by_record_time_lambda.csv`
- `section_25_errors.csv`
- `section_25_summary.json`

## Linked Graph

![cold regularization probe cold regularization probe](section_25_cold_regularization_probe.png)
