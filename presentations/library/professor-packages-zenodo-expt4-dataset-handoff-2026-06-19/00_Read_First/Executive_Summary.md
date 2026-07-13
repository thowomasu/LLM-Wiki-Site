# Executive Summary

## Dataset

LG M50T 21700 degradation study, Expt 4 drive-cycle aging is part of a public lithium-ion battery ageing dataset for commercial 21700 cells.
The Zenodo record describes commercial LG M50T / LG GBM50T2170 cells aged under different temperatures and state-of-charge ranges.
Experiment 4 is the 0-100 percent drive-cycle discharge ageing case.

For this local work, the Expt4 zip checksum matched the MD5 published by Zenodo.
So the source file is not the weak point.

## Analysis Done

The pipeline used three main evidence tracks:

1. GITT voltage curves
2. Discharge voltage curves
3. Hybrid current-pulse voltage curves

The GITT path extracts a pulse window, fits a time-domain DRT-like relaxation model, and summarizes resistance-like features.
The discharge and hybrid paths extract health-related voltage and pulse features.
The output is then compared against dataset health labels such as SOH, C/10 capacity, and 0.1 second resistance.

## Main Results

- Expt4 processed time-series files were discovered and parsed.
- GITT fitting worked on a batch of 40 files with no batch errors in the current run.
- GITT `r0_ohm` strongly tracks the dataset's 0.1 second resistance label.
- Some voltage and pulse summaries predict SOH and C/10 capacity under grouped internal validation.
- A stricter leakage audit found that some features are basically target proxies.

## What This Means

Defensible:

- The Expt4 dataset can support an internal battery health feature benchmark.
- The pipeline can parse, align, and summarize GITT, discharge, and hybrid-pulse files.
- The validation audit is useful because it catches inflated claims.

Not defensible:

- Claiming EIS validation.
- Claiming recovered DRT peaks are physically validated.
- Claiming hybrid-pulse features independently predict SOH or capacity without proxy leakage.
- Claiming DRT bands alone drive the result.

## Best Next Step

Use a locked comparison:

1. `R0 only`
2. `DRT bands without R0`
3. `R0 plus DRT bands`

Use leave-one-temperature-out as the headline test.
If the feature set fails there, it is not robust.
