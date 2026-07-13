# Method And Limits

## What The Pipeline Does

The script scans LG M50T 21700 degradation study, Expt 4 drive-cycle aging processed time-series files, selects GITT pulse/rest windows, fits a time-domain RC-kernel DRT-like model, extracts discharge-curve and hybrid-pulse health features, and exports reports, plots, CSV tables, and JSON summaries.

## What The Pipeline Does Not Prove

- It does not prove that the recovered gamma curve equals an EIS-derived DRT curve.
- It does not prove that every peak maps to one physical electrochemical process.
- It does not make raw BioLogic files the main analysis track yet.
- It does not make constant-current discharge files good DRT inputs.
- It does not call hybrid pulse summaries DRT unless the pulse/rest segmentation is upgraded and validated.
- It does not make held-out health-label prediction equivalent to EIS validation.

## Why GITT Is The DRT Track

GITT has clearer pulse and rest structure than drive-cycle traces.
That structure gives the window finder and RC relaxation model something identifiable to fit.
Constant-current discharge has ageing value, but weak pulse/rest excitation.
Hybrid pulse traces have dynamic-response value, but they need their own segmentation and validation before DRT claims are safe.

## How To Read The DRT Outputs

Use voltage RMSE as a basic fit check.
Then inspect model sensitivity before trusting peak tau.
Broad tau-band sums are safer than single peak stories because peak locations can move with baseline and regularization.

## Weak Spot You Should Not Hide

No EIS-derived comparison target was found in the inspected Expt4 folders.
That means the current claim is engineering feasibility and feature extraction, not full validation.
The strongest honest validation inside Expt4 is whether the combined GITT, discharge, and hybrid features predict held-out health labels and trend consistently across ageing.
