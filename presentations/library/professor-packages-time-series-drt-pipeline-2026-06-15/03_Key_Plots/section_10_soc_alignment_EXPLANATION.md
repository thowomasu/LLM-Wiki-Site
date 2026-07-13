# Graph Explanation: EIS 2D DRT surface Soc Alignment

Graph file: `section_10_soc_alignment.png`

Folder: `Package_Key_Plots`
## What This Figure Shows

This figure checks whether the selected pulse windows actually line up with the EIS SOC labels.

It usually shows:

- target EIS SOC labels
- SOC estimated by coulomb counting
- SOC error in percentage points
- pre-rest voltage ordering of candidate windows

## What We Can Learn

This graph tests the matched-pair assumption. If a pulse selected for 70 percent SOC looks more like a different SOC under coulomb counting, then a weak EIS comparison may be partly a matching problem.

In the current result, some SOC points are close, but the 70 percent case is noticeably approximate under simple coulomb counting.

## Why It Matters

Time-domain versus EIS comparison only makes sense if both measurements describe the same battery state. SOC mismatch can make a good method look bad, or make a bad method look accidentally good.

## Caveat

Coulomb counting here depends on the chosen anchor and capacity estimate. Protocol-confirmed SOC metadata would be better.

## What To Check Next

Use this plot before trusting a comparison plot. If SOC alignment is poor, do not overinterpret EIS disagreement as purely a DRT-model failure.
