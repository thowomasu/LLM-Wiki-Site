# Graph Explanation: time-series 2D DRT surface Held Out Cell Validation

Graph file: `section_9_held_out_cell_validation.png`

## What This Figure Shows

This graph checks whether Zenodo GITT features can predict held-out cell health labels better than a train-mean baseline.

## How To Read It

Positive skill means the small ridge model beat the baseline. Negative skill means the feature set made prediction worse. The SoH scatter panel should sit near the identity line if the DRT plus R0 feature set is useful.

## What We Can Learn

This is internal health-feature validation. It asks whether the extracted features generalize across cells.

## Caveat

This is not EIS validation. Also, with only 40 rows, large-looking skill can still be brittle. Temperature leakage is the obvious trap.
