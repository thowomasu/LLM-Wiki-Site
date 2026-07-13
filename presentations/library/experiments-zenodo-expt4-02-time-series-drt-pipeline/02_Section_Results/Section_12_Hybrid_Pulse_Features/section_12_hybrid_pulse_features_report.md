# LG M50T 21700 Expt 4 drive-cycle aging Time-Series DRT Pipeline, multi-cell 2D batch check

## Purpose

This section extracts features from the hybrid CC-pulse files.
These traces have excitation, but the current DRT window finder does not treat them as clean GITT-style pulse/rest experiments.

## Results

- Files requested: 80
- Files completed: 80
- Files errored: 0
- Rate counts: `{"0p5c": 40, "1c": 40}`
- Hybrid segments total: 17983
- Accepted hybrid segments total: 17801
- Median accepted segments per file: 165.0

## Outputs

- `section_12_hybrid_pulse_features.csv`: one row per hybrid file.
- `section_12_hybrid_pulse_segments.csv`: one row per detected hybrid current segment.
- `section_12_hybrid_pulse_errors.csv`: segmentation/load errors.

## Interpretation

Hybrid pulse data is now segmented into auditable dynamic-response windows.
This still is not hybrid DRT. It is the prerequisite segmentation work before any DRT attempt would be defensible.
