# LG M50T 21700 Expt 4 drive-cycle aging Time-Series DRT Pipeline, EIS 2D DRT surface

## Purpose

This section checks whether the fitted features move in consistent directions inside each cell as ageing progresses.

## Outputs

- `section_10_trend_consistency_correlations.csv`
- `section_10_expected_direction_checks.csv`
- `section_10_trend_consistency_summary.json`
- `section_10_trend_consistency.png`

## Results

- Correlation rows: 160
- Expected-direction checks: 32
- Expected-direction pass ratio: 0.875

## Interpretation

This is a sanity check for feature stability over RPT ageing points.
A viable health-feature pipeline should not need every cell to be perfect, but it should not have random sign flips everywhere either.
If DRT band mass trends are weaker than R0 trends, say that plainly. R0 may be carrying most of the useful signal.
