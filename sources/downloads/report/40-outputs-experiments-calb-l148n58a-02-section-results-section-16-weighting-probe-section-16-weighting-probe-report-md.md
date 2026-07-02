# CALB L148N58A, weighting probe Weighting Probe

## Purpose

Probe whether changing the EIS block weight in the combined inverse problem fixes the failure-mode audit failure pattern.

## Result

- Cases: 22
- Probe rows: 110
- Error count: 0
- Best weight by median delta: 0.03
- Best median delta: 0.01931990221947468
- Best median combined correlation: -0.030908314442907946

## Weight Summary

| EIS weight | Rows | Quality-pass | Combined corr | Delta corr | Large gains | Large losses |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.03 | 22 | 22 | -0.030908314442907946 | 0.01931990221947468 | 3 | 5 |
| 0.1 | 22 | 22 | -0.03597767883435455 | 0.013381318000501161 | 2 | 6 |
| 0.3 | 22 | 22 | -0.02348524974202172 | -0.003990946816835112 | 2 | 8 |
| 1.0 | 22 | 22 | -0.015752556467473387 | 0.013246449765722037 | 1 | 9 |
| 3.0 | 22 | 19 | -0.02132317492476548 | -0.0014076620571281326 | 0 | 7 |

## Blunt Read

If the best weight still leaves weak or negative median combined correlation, weighting alone is not enough.
If lower EIS weight prevents large losses, the current combined objective is over-constraining gamma toward the EIS baseline for some low-OCV cases.

## Outputs

- `section_16_weighting_probe_rows.csv`
- `section_16_by_weight.csv`
- `section_16_by_temperature_weight.csv`
- `section_16_errors.csv`
- `section_16_summary.json`

## Linked Graph

![weighting probe weighting probe](section_16_weighting_probe.png)
