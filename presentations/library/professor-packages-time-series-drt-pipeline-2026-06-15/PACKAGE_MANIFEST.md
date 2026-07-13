# Package Manifest

## Folder Layout

```text
00_Read_First/
```

Professor-facing summary files: viability report, rough handoff, and HTML
copies for quick reading. New plain-English files are included here:

- `PLAIN_ENGLISH_OVERVIEW.md`
- `DRIVE_CYCLE_DATASET_RECOMMENDATION.md`

```text
01_Method_And_Math/
```

Method explanation, assumptions, code notes, line-range code walkthrough, and
LaTeX-rendered math HTML.

```text
02_Key_Results/
```

Core result reports and compact CSV/JSON summaries. This includes model-rule,
DIB batch, SOC mapping, model sensitivity, Cell28 sweep, validation diagnostics,
and SOC alignment summaries.

```text
03_Key_Plots/
```

Selected PNG plots for quick visual inspection. These were regenerated with
Matplotlib from saved CSV/JSON outputs. `PLOT_GUIDE.md` explains every plot.

```text
04_Code/
```

The Python scripts needed to inspect or rerun the pipeline.

```text
05_Reproduction/
```

Runner logs and machine-readable run summaries.

## Deliberately Excluded

- Raw DIB data files.
- Large selected-window CSVs.
- Per-SOC EIS DRT curve dumps except where compact summaries are useful.
- Local dependency folders such as `.deps`.

## Current Evidence Level

Evidence supports: engineering scaffold is viable.

Evidence does not support: time-series DRT is validated as an EIS replacement.

The current saved rule-selected EIS agreement is weak, with median correlation
around 0.141.

Dataset correction: DIB should not be presented as the main drive-cycle dataset.
Use DIB for the EIS/pulse prototype, and use a drive-cycle dataset such as CALCE
dynamic profiles for the drive-cycle part.
