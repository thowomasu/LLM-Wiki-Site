# CALB L148N58A, candidate-alignment probe Candidate Alignment Probe

## Purpose

Test whether nearest-OCV HPPC pulse selection is the reason low-OCV combined DRT results stay weak.

## Result

- Cases: 22
- Candidate fits: 110
- Error count: 0
- Best candidate was nearest-OCV in 22 cases.
- Median nearest combined correlation: -0.030908314442907946
- Median best nearby combined correlation: -0.030908314442907946
- Median best-minus-nearest correlation: 0.0

## Temperature Summary

| Temperature | Cases | Best is nearest | Nearest corr | Best nearby corr | Gain | Best abs OCV delta V |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 25 C | 11 | 11 | 0.4899021361496996 | 0.4899021361496996 | 0.0 | 0.0033391229248045384 |
| 40 C | 11 | 11 | -0.034419663372559625 | -0.034419663372559625 | 0.0 | 0.002829170623779298 |

## Blunt Read

If best nearby candidates beat nearest-OCV candidates by a lot, OCV-only alignment is too naive.
If the gain is still weak, the model form or EIS/time-domain compatibility is the bigger problem.

## Outputs

- `section_17_alignment_candidate_rows.csv`
- `section_17_alignment_case_summary.csv`
- `section_17_alignment_temperature_summary.csv`
- `section_17_alignment_errors.csv`
- `section_17_summary.json`

## Linked Graph

![candidate-alignment probe candidate alignment probe](section_17_candidate_alignment_probe.png)
