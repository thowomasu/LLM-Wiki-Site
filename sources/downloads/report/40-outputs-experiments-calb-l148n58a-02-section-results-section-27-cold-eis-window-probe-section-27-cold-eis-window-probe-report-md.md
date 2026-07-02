# CALB L148N58A, cold EIS-window probe Cold EIS Window Probe

## Purpose

Test whether 10 C strict-match failure is fixed by cold-specific EIS frequency trimming plus EIS regularization.

## Result

- Temperature tested: 10 C
- Protocols: HPPC_1C, HPPC_C3
- Cells attempted per protocol: 11
- Row count: 2214
- Error count: 0
- Best variant summary: `{'variant': 'ge_0p03hz_le_50hz_lam_3', 'fmin_hz': 0.03, 'fmax_hz': 50.0, 'eis_lambda': 3.0, 'rows': 82, 'quality_pass_rows': 56, 'quality_pass_fraction': 0.6829268292682927, 'median_corr_quality': 0.928248017443013, 'corr_ge_0p75_rows_quality': 56, 'corr_ge_0p75_fraction_quality': 1.0, 'median_scaled_rmse_quality': 0.3725551306121031, 'median_time_rmse_mv_quality': 6.077196430384479}`
- Verdict: `cold_eis_window_high_corr_but_insufficient_coverage`

## Top Variant Summary

| Variant | Quality-pass fraction | Median corr | Corr >= 0.75 fraction | Median time RMSE mV |
| --- | ---: | ---: | ---: | ---: |
| ge_0p03hz_le_50hz_lam_3 | 0.6829268292682927 | 0.928248017443013 | 1.0 | 6.077196430384479 |
| ge_0p03hz_le_50hz_lam_0p1 | 0.6829268292682927 | 0.927975781232299 | 1.0 | 6.077196430384479 |
| ge_0p03hz_le_100hz_lam_3 | 0.6829268292682927 | 0.9147714458943084 | 1.0 | 6.077196430384479 |
| ge_0p03hz_le_100hz_lam_0p1 | 0.6829268292682927 | 0.9143491389658255 | 1.0 | 6.077196430384479 |
| ge_0p1hz_le_50hz_lam_0p1 | 0.5365853658536586 | 0.8956851969629319 | 1.0 | 8.781368477773288 |
| ge_0p1hz_le_50hz_lam_3 | 0.5365853658536586 | 0.8948530615942532 | 1.0 | 8.781368477773288 |
| ge_0p1hz_le_100hz_lam_0p1 | 0.5365853658536586 | 0.8828576965467121 | 1.0 | 8.781368477773288 |
| ge_0p03hz_all_lam_0p1 | 0.6829268292682927 | 0.8791278102190256 | 1.0 | 6.077196430384479 |
| ge_0p1hz_le_100hz_lam_3 | 0.5365853658536586 | 0.8691586540742156 | 1.0 | 8.781368477773288 |
| ge_0p03hz_all_lam_3 | 0.6829268292682927 | 0.8502616260328226 | 1.0 | 6.077196430384479 |
| ge_0p1hz_all_lam_0p1 | 0.5365853658536586 | 0.8245567865557367 | 0.8181818181818182 | 8.781368477773288 |
| ge_0p03hz_le_50hz_lam_30 | 0.6829268292682927 | 0.7373236459666659 | 0.10714285714285714 | 6.077196430384479 |

## Blunt Read

A valid cold EIS preprocessing fix needs high median correlation and broad quality-pass coverage.
If high correlation appears only after trimming away comparability or leaving many rows outside the gate, it is not solved.

## Outputs

- `section_27_variant_rows.csv`
- `section_27_by_variant.csv`
- `section_27_by_record_variant.csv`
- `section_27_by_protocol_variant.csv`
- `section_27_errors.csv`
- `section_27_summary.json`

## Linked Graph

![cold EIS-window probe cold EIS window probe](section_27_cold_eis_window_probe.png)
