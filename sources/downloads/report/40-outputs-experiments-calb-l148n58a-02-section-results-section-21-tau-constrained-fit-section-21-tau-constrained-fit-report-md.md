# CALB L148N58A, tau-constrained pulse-to-EIS fit Tau-Constrained Fit

## Purpose

Test whether forcing the HPPC time-domain DRT tau grid into the EIS tau range improves bridge agreement.

## Result

- Rows: 123
- Quality-pass rows: 99
- Median default correlation: -0.0485998081564577
- Median constrained correlation: 0.8956430786264292
- Median constrained-minus-default correlation: 0.6464111745046026
- Constrained-better rows: 97

## EIS Record Summary

| EIS record | Rows | Quality-pass | Default corr | Constrained corr | Delta | Constrained better | Default RMSE mV | Constrained RMSE mV |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 33 | 33 | -0.05445886101561304 | -0.02803692935162186 | 0.028966445737189633 | 33 | 2.681264689930457 | 2.977150507952471 |
| 1 | 33 | 33 | -0.04774406026887051 | 0.8961991078997222 | 0.9101022654390495 | 33 | 0.8446204754100032 | 1.3081595219603253 |
| 2 | 33 | 33 | -0.0363857034904722 | 0.9103864097541238 | 0.9452981280017861 | 31 | 0.39914624123564024 | 2.240935241084275 |
| 3 | 24 | 0 | None | None | None | 0 | None | None |

## Blunt Read

If constraining tau improves correlation but makes voltage RMSE worse, the default fit was hiding mismatch in slow modes.
If it does not improve correlation, the failure is deeper than tau support.

## Outputs

- `section_21_tau_constrained_rows.csv`
- `section_21_by_eis_record.csv`
- `section_21_by_temperature.csv`
- `section_21_errors.csv`
- `section_21_summary.json`

## Linked Graph

![tau-constrained pulse-to-EIS fit tau constrained fit](section_21_tau_constrained_fit.png)
