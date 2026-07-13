# Viability Report

## Verdict

- Engineering scaffold: research_scaffold_viable
- Scientific method: not_validated

Plain English: the prototype is viable enough to keep researching. It is not viable as a final battery-health model or as proof that time-series DRT can replace EIS.

## What Passes

- Synthetic inverse check: pass, RMSE 0.8007 mV.
- DIB batch runner: pass, 15 rows, 0 errors, 15 quality-pass rows.
- SOC mapping sensitivity: pass, 4 modes, 0 errors.
- Model sensitivity: pass, 120 rows, 0 errors, 112 quality-pass rows.
- Pre-declared model rule: pass, 10 selected rows, 0 errors, 10 quality-pass rows.

## What Fails Scientifically

- Batch median EIS correlation is only 0.1046.
- Pre-declared rule median EIS correlation is 0.1407 and median normalized RMSE is 0.9784.
- SOC mapping changed the selected candidate for 0 targets in the first sensitivity run.
- Model sensitivity found 10 targets whose correlation range changes by more than 0.1 across baseline/lambda settings.
- Median model-setting correlation is 0.2017 and median normalized RMSE is 0.4354.

This means the pipeline can produce curves, but the curve shape is still too dependent on assumptions.

## Keep Doing

- Use the current code to test matched-pair cases across cells.
- Treat SOC mapping, baseline mode, and lambda as explicit assumptions.
- Use the pre-declared model-rule output before looking at EIS performance.
- Report voltage fit, EIS shape agreement, quality flags, and sensitivity ranges together.

## Do Not Do Yet

- Do not train a foundation model on these labels as ground truth.
- Do not claim the time-domain DRT is validated against EIS.
- Do not choose `lambda` or baseline mode by picking the prettiest EIS comparison after the fact.

## Next Required Step

Run the pre-declared model rule on more cells after the protocol metadata is confirmed. If the rule-selected outputs still disagree with EIS, the method is not validated. Do not move the goalposts.

Blunt version: the code is now useful. The science is still guilty until proven innocent.
