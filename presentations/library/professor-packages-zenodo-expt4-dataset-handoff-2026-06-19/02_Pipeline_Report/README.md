# Pipeline Report

This folder contains the main analysis output.

## Fast Entry Points

| File or folder | What it is |
|---|---|
| `pipeline_readme.md` | Original pipeline README copied from the workspace. |
| `index.html` | Browser report entry point. Open this if HTML rendering is preferred. |
| `pipeline_summary.json` | Machine-readable summary of all sections. |
| `00_Docs/` | Method, limits, report index, and reproduction docs from the pipeline run. |
| `01_Graphs/` | Graph folder copied beside `index.html` so browser links work. |
| `02_Section_Results/` | Full section outputs: reports, CSVs, JSONs, and plots. |

## Section Order

1. Data audit
2. File screen
3. GITT window finder
4. GITT candidate fit
5. GITT batch
6. Model sensitivity
7. Raw conversion check
8. Health label join
9. Held-out cell validation
10. Trend consistency
11. Discharge-curve features
12. Hybrid-pulse features
13. Multi-protocol validation

## What To Watch For

The pipeline report is descriptive.
The validation audit is more critical.
Read `../04_Validation_Audit/README.md` before making claims.
