# Graph Explanation: time-series 2D DRT surface Validation Diagnostics

Graph file: `section_9_validation_diagnostics.png`

Folder: `Package_Key_Plots`
## What This Figure Shows

This figure asks whether weak EIS agreement is just a scale problem or a deeper shape problem. It also shows how lambda, the smoothness setting, changes the comparison.

Typical panels include:

- best scale factors between time-domain and EIS gamma
- normalized shape error after scaling
- correlation or RMSE across lambda values
- diagnostics for the 70 percent SOC case

## What We Can Learn

If one constant scale factor fixed the mismatch, the problem might be a simple magnitude calibration issue. The current diagnostics suggest it is not that simple. Shape disagreement remains important.

Lambda matters too. Smoothing can make a curve look more EIS-like, but that does not prove the smoother curve is more true. If lambda is picked after looking at EIS, validation is biased.

## Why It Matters

This plot is a guard against a lazy explanation. It stops us from saying "the curves only need rescaling" when the shape evidence does not support that.

## Caveat

Smoother is not automatically more correct. Heavy smoothing can hide real structure.

## What To Check Next

Use the pre-declared model-rule plot. Sensitivity diagnostics can teach us where the method is weak, but the model rule is the more honest validation check because it selects settings before EIS scoring.
