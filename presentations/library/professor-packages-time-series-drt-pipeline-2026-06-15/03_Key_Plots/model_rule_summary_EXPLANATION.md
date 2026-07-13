# Graph Explanation: Model Rule Summary

Graph file: `model_rule_summary.png`

Folder: `Package_Key_Plots`
## What This Figure Shows

This figure shows the result after applying the pre-declared model-selection rule.

The rule selects lambda using time-domain information only:

- voltage RMSE
- gamma roughness
- fast/mid/slow band stability
- penalties for edge lambda values or nearly flat gamma

EIS agreement is checked after selection, not during selection.

## How To Read It

First check which lambda values the rule selected. Then check voltage RMSE to make sure the selected models still reconstruct voltage. Finally check EIS correlation and normalized RMSE.

If EIS agreement is weak after the rule, that is an honest weak result. Do not treat it as a presentation problem.

## What We Can Learn

The current rule-selected EIS agreement is still weak. That is bad news scientifically, but good news methodologically: it means the pipeline is no longer hiding behind after-the-fact lambda selection.

## Why It Matters

This is the fairest validation plot in the current package. It asks: if we choose model settings before looking at EIS, does the time-domain DRT still agree? Right now, not strongly enough.

## Caveat

An honest rule can still fail. That is useful because it tells us the method needs more work instead of just better presentation.

## What To Check Next

Run the same rule on more cells and SOH labels after protocol metadata is confirmed. If the rule-selected results still disagree with EIS, the method is not validated.
