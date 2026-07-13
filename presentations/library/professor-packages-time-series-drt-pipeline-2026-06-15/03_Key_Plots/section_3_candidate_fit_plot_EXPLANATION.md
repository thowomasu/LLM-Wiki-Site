# Graph Explanation: HPPC window finder Candidate Fit Plot

Graph file: `section_3_candidate_fit_plot.png`

Folder: `Package_Key_Plots`
## What This Figure Shows

This figure shows the actual time-domain fit for one selected pulse/rest window.

Read it panel by panel:

- The current panel shows the excitation the solver sees.
- The voltage panel compares measured voltage against reconstructed voltage.
- The DRT panel shows resistance weight versus tau.
- The residual panel shows measured minus fitted voltage in millivolts.

This is where the pipeline moves from "this window looks usable" to "the solver can or cannot explain this voltage response."

## How To Read It

Start with current. If the current does not contain a clear pulse/rest event, the DRT fit is weak before it starts.

Then look at voltage reconstruction. The fitted voltage should follow the measured voltage through the pulse and the relaxation period. Next look at the residual. A good residual should be small and not show obvious leftover pulse structure.

Finally, read the DRT curve. A peak at small tau means fast relaxation. A peak at larger tau means slower relaxation. A boundary peak near the maximum tau is suspicious because it may mean the window is too short or the baseline is leaking into gamma.

## What We Can Learn

This graph tells us whether the local voltage fit is mechanically credible. If voltage RMSE is bad, the DRT curve should not be trusted at all.

If voltage RMSE is good, the result is only partly encouraging. It means the model can reconstruct voltage, not that the gamma shape is physically correct. Baseline terms and lambda can still move resistance between fast, mid, and slow tau ranges.

## Why It Matters

This is the most tempting plot to overread. A smooth DRT curve next to a nice voltage fit feels convincing. Do not fall for that. The real validation question comes later: does this gamma shape agree with EIS under a pre-declared model rule?

## Caveat

Small voltage error is necessary, but not sufficient. A model can fit voltage well while still assigning the wrong gamma shape, especially if baseline drift or regularization is wrong.

## What To Check Next

Compare this graph with the EIS comparison plot for the same cell, SOC, and condition. If the voltage fit is good but the EIS shape match is weak, the honest conclusion is that voltage fitting alone is not enough.
