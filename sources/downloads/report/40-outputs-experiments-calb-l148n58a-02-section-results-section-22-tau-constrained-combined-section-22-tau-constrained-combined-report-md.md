# CALB L148N58A, tau-constrained combined fit Tau-Constrained Combined Fit

## Purpose

Apply the tau-constrained pulse-to-EIS fit EIS-tau constraint to the paper-style combined EIS plus HPPC inverse problem.

## Result

- Rows: 123
- Quality-pass rows: 66
- Median separate tau-constrained correlation: 0.9020779325037587
- Median combined tau-constrained correlation: 0.4774624058504997
- Median combined-minus-separate correlation: -0.34825037739296205
- Combined-better rows: 12

## EIS Record Summary

| EIS record | Rows | Quality-pass | Separate corr | Combined corr | Delta | Combined better | Separate RMSE mV | Combined RMSE mV |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 33 | 22 | -0.025960063906899734 | 0.2743532207815203 | 0.0011440375625019015 | 12 | 2.8674522675483143 | 3.760345285803683 |
| 1 | 33 | 22 | 0.9066836454630784 | 0.49105414773812894 | -0.4154339674771425 | 0 | 1.142453367838411 | 2.19765675128813 |
| 2 | 33 | 22 | 0.9139766810155827 | 0.573205061328913 | -0.34991472520380246 | 0 | 1.447222020145647 | 2.3230244250312078 |
| 3 | 24 | 0 | None | None | None | 0 | None | None |

## Blunt Read

The key comparison is tau-constrained pulse-to-EIS fit separate constrained versus this combined constrained objective.
If combined does not beat separate, the paper-style objective still needs better weighting or constraints before it earns trust.

## Outputs

- `section_22_tau_constrained_combined_rows.csv`
- `section_22_by_eis_record.csv`
- `section_22_by_temperature.csv`
- `section_22_errors.csv`
- `section_22_summary.json`

## Linked Graph

![tau-constrained combined fit tau constrained combined](section_22_tau_constrained_combined.png)
