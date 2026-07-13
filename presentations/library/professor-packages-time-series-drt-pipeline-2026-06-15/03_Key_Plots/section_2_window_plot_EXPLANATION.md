# Graph Explanation: file and protocol screen Window Plot

Graph file: `section_2_window_plot.png`

Folder: `Package_Key_Plots`
## What This Figure Shows

This figure explains the input-selection step. The pipeline is not fitting DRT yet. It is deciding which parts of the time-series file are even worth fitting.

Read it like this:

- The current trace shows when the cell is being excited by a pulse.
- The voltage trace shows the cell response to that current.
- Shaded regions mark candidate pulse windows.
- Accepted windows should have a clear current step, enough pulse duration, and enough rest afterward.

For sections where raw full DIB traces are unavailable in this vault, the replacement plot summarizes the saved candidate table instead of pretending to redraw missing raw data.

## How To Read It

Look for pulse/rest structure. A useful time-domain DRT window needs the current to change enough to create a measurable voltage response, then it needs rest afterward so relaxation is visible. If the current barely changes, or if there is no rest period, the solver has very little information about tau.

Also check whether the selected windows are low-current discharge pulses. Those are preferred because they are less aggressive than high-current capacity segments and are closer to the small-signal spirit of EIS. Closer does not mean identical.

## What We Can Learn

The graph tells us whether the pipeline is feeding the solver reasonable windows. Bad windows can still produce a gamma curve, but that curve would mostly be math theater. The point of this plot is to block that failure early.

## Why It Matters

Window selection is one of the biggest ways this method can fool you. If the selected pulse is not actually comparable to the EIS condition, then the later DRT comparison is already compromised.

## Caveat

Window finding is screening. It says a window is plausible. It does not prove the fitted DRT is correct.

## What To Check Next

Open the matching candidate-fit plot. This window plot tells you whether a pulse was a reasonable input. The candidate-fit plot tells you whether the model could reconstruct voltage inside that selected input.
