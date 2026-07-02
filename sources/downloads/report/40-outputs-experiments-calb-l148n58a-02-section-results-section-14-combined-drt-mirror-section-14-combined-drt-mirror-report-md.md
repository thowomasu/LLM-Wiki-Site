# CALB L148N58A, combined DRT mirror check Combined DRT Mirror

## Purpose

Mirror the multi-temperature 2D batch check batch using the paper-aligned combined EIS plus time-domain inverse problem.

## Result

- Temperatures: 10 C, 25 C, 40 C
- Cells attempted per temperature: 11
- Comparison rows: 123
- Quality-pass rows: 71
- Error count: 0
- Median separate post-hoc gamma correlation: -0.04774406026887051
- Median combined gamma correlation: -0.01587805529887068
- Median combined-minus-separate correlation: 0.02948255678110624

## Temperature Summary

| Temperature | Rows | Quality-pass | Separate corr | Combined corr | Delta corr | Combined time RMSE mV |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 10 C | 41 | 5 | -0.05115965726126483 | 0.1454286867615428 | 0.03304164011943431 | 6.9905610887485405 |
| 25 C | 38 | 33 | -0.014459186812620282 | -0.009786677075445277 | 0.005186584105629437 | 2.9152145308451236 |
| 40 C | 44 | 33 | -0.05879878660274218 | -0.018544999826251914 | 0.039351647205745854 | 2.7908905924782914 |

## Critical Read

This is the fair test of whether the new paper math changes the result.
If the combined-minus-separate correlation is small or negative, the stronger inverse problem did not fix the bridge.
That would be useful, not embarrassing. It means the bottleneck is probably alignment, weighting, preprocessing, or model mismatch.

## Outputs

- `section_14_combined_drt_mirror_summary.csv`
- `section_14_combined_drt_mirror_overlap_long.csv`
- `section_14_combined_drt_mirror_errors.csv`
- `section_14_temperature_summary.csv`
- `section_14_summary.json`

## Linked Graph

![combined DRT mirror check combined DRT mirror](section_14_combined_drt_mirror.png)
