# CALB L148N58A, lambda sensitivity check Model/Lambda Sensitivity

## Purpose

Check whether the HPPC time-domain DRT shape is stable under regularization changes.

## Result

- Best post-hoc EIS correlation lambda: 3.0 with corr -0.06290097176658203.
- Best voltage RMSE lambda: 0.003 with RMSE 1.60601 mV.

## Critical Read

A lambda that improves EIS agreement after looking at EIS is not a valid selection rule. Use this as a diagnostic, not proof.
If voltage RMSE barely changes while gamma shape changes a lot, the inverse problem is underdetermined.

## Linked Graph

![lambda sensitivity check lambda sensitivity](section_7_lambda_sensitivity.png)
