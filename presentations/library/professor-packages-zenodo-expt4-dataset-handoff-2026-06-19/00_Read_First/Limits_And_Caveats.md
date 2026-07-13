# Limits And Caveats

This is the part that stops the analysis from becoming nonsense.

## Biggest Risk

Some features leak the answer.

Examples:

- Capacity-like features predict capacity because they are capacity.
- Duration-per-capacity features contain measured capacity in the denominator.
- Hybrid pulse transition counts can mostly track how long the cell lasted before cutoff.
- `gitt_r0_ohm` is useful for resistance, but it is not a DRT peak feature.

If these are treated as independent predictors, the model looks smarter than it is.

## DRT Limit

The GITT fit is DRT-like in the time domain.
It is not validated against measured EIS DRT in this package.

That matters.
Without an EIS comparison target, the DRT peak locations are model outputs, not proven physical assignments.

## Validation Limit

Leave-one-cell-out is useful, but it can still share too much structure across the same dataset.
Leave-one-temperature-out is harsher and more honest.

If a result only looks strong in leave-one-cell-out and weakens under leave-one-temperature-out, do not oversell it.

## What The Professor Should Judge

Judge this package as:

- A data parsing and feature engineering pipeline.
- A first internal validation benchmark.
- A starting point for a stricter experiment.

Do not judge it as:

- A finished DRT physics validation.
- A proof that hybrid pulse data independently estimates SOH.
- A paper-ready claim without another validation target.
