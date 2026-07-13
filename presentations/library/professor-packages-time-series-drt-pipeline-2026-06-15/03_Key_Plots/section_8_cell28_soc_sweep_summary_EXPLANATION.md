# Graph Explanation: combined EIS and time-domain DRT prototype Cell28 Soc Sweep Summary

Graph file: `section_8_cell28_soc_sweep_summary.png`

Folder: `Package_Key_Plots`
## What This Figure Shows

This summary compares Cell28 across several SOC labels instead of relying on one hand-picked case.

The panels summarize:

- EIS/time-domain shape correlation by SOC.
- Voltage reconstruction RMSE by SOC.
- Time-domain DRT area by SOC.
- EIS DRT area by SOC.

The point is to see whether behavior is consistent across 95, 70, 50, 20, and 5 percent SOC.

## How To Read It

Start with voltage RMSE. If RMSE is high at one SOC, that local fit is weak. Then check correlation. Good voltage RMSE with weak correlation means the model fits voltage but does not reproduce the EIS-derived DRT shape.

Then compare time-domain area and EIS area. If areas move in unrelated ways across SOC, the methods are not agreeing on how resistance distribution changes with SOC.

## What We Can Learn

The current sweep is useful because it prevents one lucky plot from carrying the whole argument. The result is not strong enough yet: voltage reconstruction is fairly good, but EIS agreement remains weak.

## Why It Matters

A method that only works at one SOC is not useful as a general battery-health tool. SOC sweep behavior tells us whether the pipeline is stable across operating state.

## Caveat

SOC labels are approximate unless protocol metadata confirms exactly which pulse belongs to which EIS SOC point.

## What To Check Next

Use this with the SOC alignment plot. If a weak SOC point also has poor SOC alignment, the comparison may be contaminated by matching error.
