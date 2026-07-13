# Graph Explanation: Model Sensitivity Summary

Graph file: `model_sensitivity_summary.png`

Folder: `Package_Key_Plots`
## What This Figure Shows

This figure shows how baseline mode and lambda change the validation metrics.

Baseline mode controls what slow voltage drift the model is allowed to explain outside gamma. Lambda controls how smooth gamma must be.

The panels usually compare:

- EIS/time-domain correlation
- normalized shape error
- voltage RMSE
- gamma area or gamma stability

## How To Read It

Look for metric spread across settings. If voltage RMSE barely changes while EIS correlation changes a lot, the recovered gamma is model-sensitive. That means the voltage signal alone is not forcing one stable DRT answer.

Also compare baseline modes. If `offset`, `charge`, and `time_charge` lead to different conclusions, then baseline/OCV handling is not a small detail. It is a core uncertainty.

## What We Can Learn

The current result is sensitive to modeling choices. That is one of the biggest weaknesses in the project. It means the method is not robust enough for a final scientific claim.

## Why It Matters

This plot is the one that should make you uncomfortable. If the result improves only after choosing a convenient baseline or lambda, that is not validation. That is tuning.

## Caveat

Do not pick the setting that looks best after seeing EIS. The rule must be chosen before EIS scoring.

## What To Check Next

Use the pre-declared model-rule plot. Model sensitivity tells us where the method can be tuned. The model rule tests what happens when we stop tuning against EIS.
