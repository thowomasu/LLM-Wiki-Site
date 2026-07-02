# CALB Package Audit

Date: 2026-06-29

## Scope

This audit covers the untracked CALB package at `40 Outputs/Experiments/CALB L148N58A/` and the CALB scripts under `scripts/experiments/calb_l148n58a/`.

It does not classify unrelated untracked Zenodo, KIT/RADAR4KIT, DRT comparison, or repo daily log files.

## Commit Readiness Verdict

The CALB package is commit-ready as a coherent generated evidence package if the commit is scoped to CALB scripts, CALB outputs, and the docs that describe the CALB boundary.

Do not use `git add .`. The worktree contains unrelated untracked project work.

## Evidence To Keep

- `00_Docs/`: claim boundary, method limits, source index, viability report, and this audit.
- `01_Manifest/`: processed CALB archive manifest, protocol summary, sample summary, and ZIP listing. These are evidence for what local data was parsed.
- `02_First_Slice/`: curated first-slice CSV extracts and summary. These are lightweight review data, not raw source replacement.
- `02_Section_Results/Section_01_*` through `Section_42_*`: section reports, section summaries, result CSVs, and audit CSVs. These are the core evidence chain.
- `01_Graphs/`: generated plots and explanation notes for reviewer inspection. Keep them because the package is meant to be professor-readable, not code-only.
- `03_Professor_Report/`: HTML presentation/report copies. Keep them as generated deliverables.
- `pipeline_summary.json`: machine-readable package index and claim-boundary summary.
- `scripts/experiments/calb_l148n58a/*.py`: reproducible experiment and audit scripts. Keep all current CALB scripts together because later sections depend on earlier section outputs and helpers.

## Generated But Useful

- PNG plots in `01_Graphs/` and duplicated section PNGs in `02_Section_Results/`: generated, but useful for review and visual QA.
- Section CSVs and JSON summaries: generated, but they are the evidence package. Treat them as durable unless the repo policy changes to store only scripts.
- HTML reports: generated, but useful professor-facing artifacts.
- `section_35_*` regression outputs: generated, but useful as the current lockfile for frozen pulse-to-EIS rule, drive-cycle ECM baseline check, external-validation claim boundary, and SOC-stratified drive-cycle audit boundaries.

## Disposable Or Not Present

No obvious disposable CALB clutter was found in this package scan:

- no CALB `__pycache__` folders
- no CALB `.pyc` files
- no CALB `.tmp`, `.bak`, `.cache`, or `.log` files
- no nonempty CALB `*errors*.csv` files

Vendor/dependency `__pycache__` folders exist under `.deps/`; those are outside the CALB package and were not removed.

## Claim Boundary

frozen pulse-to-EIS rule is the defensible internal CALB pulse-bridge result: 246 of 246 quality-pass rows across 10, 25, and 40 C, with 2 narrow EIS-lambda fallback rows.

drive-cycle ECM baseline check limits the drive-cycle claim: fixed HPPC-derived DRT loses to the stronger drive-cycle-fitted ECM baseline.

SOC-stratified drive-cycle audit limits the drive-cycle claim again: only 16 of 198 drive-cycle rows are within 5 percent SOC delta, and the aligned subset still does not beat the best ECM baseline.

External validation is still blocked. external-validation claim boundary reports missing or insufficient same-cell EIS pairing in the current local external evidence.

## Conservative Staging Recommendation

Stage CALB work by path, not by repo-wide wildcard:

```powershell
git add README.md HANDOFF.md "00 Meta/Handoff/05 Next Steps.md" "00 Meta/Handoff/06 Time-Series DRT Pipeline.md" "00 Meta/Health Checks.md"
git add "40 Outputs/Experiments/CALB L148N58A"
git add scripts/experiments/calb_l148n58a
```

Review unrelated modified wiki indexes and non-CALB untracked work separately.
