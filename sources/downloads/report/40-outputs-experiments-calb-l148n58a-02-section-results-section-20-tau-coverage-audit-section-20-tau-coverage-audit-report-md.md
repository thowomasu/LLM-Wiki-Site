# CALB L148N58A, tau-coverage audit Tau Coverage Audit

## Purpose

Check whether HPPC time-domain gamma is being fitted outside the tau range where EIS DRT is available.

## Result

- Rows: 123
- Quality-pass rows: 99
- Median time gamma fraction above EIS tau max: 0.27327271120524804
- Median time gamma fraction inside EIS tau window: 0.710135303228249
- Median HPPC/EIS overlap correlation: -0.0485998081564577

## EIS Record Summary

| EIS record | Rows | Quality-pass | Corr | Fraction inside | Fraction above | Time peak tau s | EIS peak tau s |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 33 | 33 | -0.05445886101561304 | 0.849717807281421 | 0.15028219271857887 | 24.47603204757505 | 47.7412329748344 |
| 1 | 33 | 33 | -0.04774406026887051 | 0.7592448297957695 | 0.16692994835491332 | 38.27419694941872 | 47.7412329748344 |
| 2 | 33 | 33 | -0.0363857034904722 | 0.3205574072138795 | 0.5366122845158666 | 53.521731495423246 | 47.7412329748344 |
| 3 | 24 | 0 | None | None | None | None | None |

## Correlation Diagnostics

- time_gamma_fraction_below_eis_window: None (n=99)
- time_gamma_fraction_overlap_eis_window: -0.3377415638810787 (n=99)
- time_gamma_fraction_above_eis_window: 0.10363609139929102 (n=99)
- time_peak_tau_s: 0.026023982163271668 (n=99)
- eis_peak_tau_s: 2.2246909391785166e-17 (n=99)

## Blunt Read

If most time-domain gamma area sits above the EIS tau range, the bridge comparison is not testing like against like.
Then the next fix is not another lambda tweak. It is a constrained time-domain tau grid or a model-form revision that prevents unresolved slow mass from absorbing baseline/OCV drift.

## Outputs

- `section_20_tau_coverage_rows.csv`
- `section_20_by_eis_record.csv`
- `section_20_by_temperature.csv`
- `section_20_correlations.csv`
- `section_20_errors.csv`
- `section_20_summary.json`

## Linked Graph

![tau-coverage audit tau coverage audit](section_20_tau_coverage_audit.png)
