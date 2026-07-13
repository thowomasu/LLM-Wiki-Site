# Dataset Map

## Source Dataset

The public dataset is hosted on Zenodo:

- Record: https://zenodo.org/records/10637534
- DOI: https://doi.org/10.5281/zenodo.10637534
- Related paper: https://doi.org/10.1016/j.jpowsour.2024.234185

The original dataset is organized by experiment.
Experiment 4 is the drive-cycle ageing control dataset.

## Local Source Layout Used By The Pipeline

The full local raw dataset is not copied into this package.
The local path used during analysis was:

```text
[local path redacted]
```

The converted and generated outputs live in the LLM Wiki workspace:

```text
40 Outputs/Experiments/LG M50T 21700 Expt 4 drive-cycle aging/
```

## Pipeline Input Families

| Family | Meaning | Used for |
|---|---|---|
| `GITT Voltage Curves` | Pulse-rest voltage curves from reference performance tests. | Time-domain DRT-like fitting and resistance features. |
| `0.1C Voltage Curves` | Slow discharge curves. | Health-related voltage and capacity-shape features. |
| `0.5C Voltage Curves` | Faster discharge curves. | Extra discharge-curve features. |
| `Hybrid CC-Pulse Voltage Curves` | Hybrid pulse and discharge tests. | Pulse and voltage features, with leakage caveats. |
| `Performance Summary` | Dataset health labels and ageing metadata. | SOH, capacity, resistance, throughput, days of degradation. |

## Current Run Counts

From the pipeline summary:

| Item | Count |
|---|---:|
| Conversion manifest rows | 305 |
| Processed time-series files | 280 |
| Raw performance-check files | 666 |
| Performance summary rows | 80 |
| GITT batch files completed | 40 |
| Discharge-curve files completed | 120 |
| Hybrid-pulse files completed | 80 |

## Important Note

The dataset itself has useful processed time-series files.
Use those first.
The raw BioLogic `.mpr` and `.mpt` files are heavier and harder to parse.
