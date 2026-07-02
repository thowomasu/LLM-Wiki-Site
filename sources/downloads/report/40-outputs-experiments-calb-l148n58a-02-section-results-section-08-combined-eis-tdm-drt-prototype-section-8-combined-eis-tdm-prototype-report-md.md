# CALB L148N58A, combined EIS and time-domain DRT prototype Combined EIS plus TDM DRT Prototype

## Purpose

Prototype the stronger paper-aligned idea: EIS and time-domain HPPC data share one nonnegative gamma vector in one regularized inverse problem.

## Result

- Status: `prototype_runs_not_validated`
- Combined time voltage RMSE: 4.08509 mV
- Combined EIS real RMSE: 8.7672e-05 ohm
- Combined EIS imaginary RMSE: 0.000119808 ohm
- Combined R0: 0 ohm
- Combined Rinf: 0.00098720132 ohm

## Critical Read

This is the first implementation of the right shape of math, not a validation result.
The block weighting, OCV handling, and OCV/SOC match still need pressure testing.
Do not claim the combined method is validated from this section.

## Outputs

- `section_8_combined_gamma.csv`
- `section_8_combined_selected_window.csv`
- `section_8_summary.json`

## Linked Graph

![combined EIS and time-domain DRT prototype combined prototype](section_8_combined_eis_tdm_prototype.png)
