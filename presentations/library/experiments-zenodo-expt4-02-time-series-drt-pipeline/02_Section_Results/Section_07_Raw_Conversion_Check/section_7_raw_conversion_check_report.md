# LG M50T 21700 Expt 4 drive-cycle aging Time-Series DRT Pipeline, lambda sensitivity check

## Purpose

This section checks whether a converted raw BioLogic CSV can be loaded by the same time-series window finder.

## Input

- Converted CSV: `[local path redacted]`

## Result

- Rows after cleaning: 78183
- Candidate windows: 3
- Accepted windows: 3

## Interpretation

The converted raw files are readable, but they are still protocol-heavy.
Use processed GITT as the main DRT track until raw protocol segmentation is made stricter.
