# CALB L148N58A, multi-cell 2D batch check Multi-Cell 2D Batch

## Purpose

Run the same time-series 2D DRT versus EIS 2D DRT comparison across multiple CALB cells at one temperature.

## Result

- Temperature: 25 C
- Cells attempted: 11
- Cells completed: 11
- Comparison rows: 38
- Quality-pass rows: 33
- Median quality-pass gamma correlation: -0.014459186812620282
- Median quality-pass absolute OCV delta: 0.004637073089599486 V

## Critical Read

This is the first repeatability check. If the batch median is weak, the method is still not validated no matter how nice one cell looks.
The quality gate rejects rows with time voltage RMSE above 10 mV or OCV mismatch above 20 mV.

## Outputs

- `section_12_multicell_2d_summary.csv`
- `section_12_multicell_2d_overlap_long.csv`
- `section_12_multicell_2d_errors.csv`
- `section_12_summary.json`

## Linked Graph

![multi-cell 2D batch check multi-cell 2D batch](section_12_multicell_2d_batch.png)
