# CALB L148N58A, multi-temperature 2D batch check Multi-Temperature 2D Batch

## Purpose

Run the same time-series 2D DRT versus EIS 2D DRT comparison across cells and CALB temperatures.

## Result

- Temperatures: 10 C, 25 C, 40 C
- Cells attempted per temperature: 11
- Comparison rows: 123
- Quality-pass rows: 99
- Error count: 0
- Median quality-pass gamma correlation: -0.0485998081564577
- Median quality-pass absolute OCV delta: 0.004673578582763849 V

## Temperature Summary

| Temperature | Rows | Quality-pass | Median corr | Median abs OCV delta V | Median time RMSE mV |
| --- | ---: | ---: | ---: | ---: | ---: |
| 10 C | 41 | 33 | -0.04935837533781184 | 0.004981905670165876 | 2.5998657767311992 |
| 25 C | 38 | 33 | -0.014459186812620282 | 0.004637073089599486 | 0.8446204754100032 |
| 40 C | 44 | 33 | -0.05879878660274218 | 0.004464933624267697 | 0.2540634829915426 |

## Critical Read

This is a broader repeatability test, not proof. The batch still uses nearest-OCV HPPC windows, not protocol-confirmed SOC alignment.
If temperature changes move the gamma correlation around, the current bridge is sensitive to assumptions and should not be used as a label generator.

## Outputs

- `section_13_multitemp_2d_summary.csv`
- `section_13_multitemp_2d_overlap_long.csv`
- `section_13_multitemp_2d_errors.csv`
- `section_13_temperature_summary.csv`
- `section_13_summary.json`

## Linked Graph

![multi-temperature 2D batch check multi-temperature 2D batch](section_13_multitemp_2d_batch.png)
