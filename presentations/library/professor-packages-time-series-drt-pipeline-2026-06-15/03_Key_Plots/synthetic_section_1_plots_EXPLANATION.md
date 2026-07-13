# Graph Explanation: Synthetic first-slice protocol inventory Plots

Graph file: `synthetic_section_1_plots.png`

Folder: `Package_Key_Plots`
## What This Figure Shows

This figure is the controlled test case. The data is synthetic, so the true resistance branches are known before the solver runs.

Read it panel by panel:

- Panel A shows the current input in amps. The current steps are the excitation that creates voltage relaxation.
- Panel B compares measured synthetic voltage with reconstructed voltage. This is the first sanity check.
- Panel C shows recovered DRT-like resistance weights across tau. Tau is relaxation time in seconds on a log scale.
- Panel D shows voltage residual in millivolts, meaning measured minus fitted voltage.
- Panel E shows the same residual as a signed percentage of measured voltage.

The top current and voltage panels use the same time span. That lets you line up each current step with the voltage response directly.

## How To Read It

Start with Panel B. If the orange fitted voltage misses the measured voltage badly, the solver has already failed. Then check Panel D. Residuals should look small and patternless, not like a hidden pulse response that the model failed to capture.

Only after that should you look at Panel C. A peak at small tau means the solver used fast relaxation. A peak at larger tau means slower relaxation. In the synthetic case, the red markers show the known truth, so the recovered curve can be judged against an actual answer key.

## What We Can Learn

This graph tells us whether the inverse math is broken before we touch real battery data. If the solver cannot recover a controlled synthetic response, it has no business being trusted on DIB data.

The important lesson is mixed. The voltage reconstruction can be strong, while the DRT recovery can still smear or shift peaks. Slow components are especially fragile because the window must be long enough to observe slow relaxation.

## Why It Matters

This is the minimum credibility test for the pipeline. Passing it does not validate the science, but failing it would kill the whole approach immediately.

## Caveat

This is a sanity check, not proof on real battery data. Synthetic data is easier because the model that generates it is close to the model used to fit it.

## What To Check Next

Use this plot to check whether the solver behaves under controlled conditions. Then move to real-data plots and ask a harsher question: does the same voltage-fitting machinery produce DRT shapes that agree with EIS without tuning after the fact?
