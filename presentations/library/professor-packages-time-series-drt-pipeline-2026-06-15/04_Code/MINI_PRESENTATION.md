# Mini Presentation: Code

## Slide 1: Results

- The folder contains the scripts needed to inspect or rerun the pipeline logic.
- Main workflow scripts cover synthetic testing, window finding, candidate fitting, EIS comparison, batch processing, sensitivity, model rule, viability reporting, plotting, and HTML export.
- The copied code is mainly for review inside the professor package.

---

## Slide 2: Achievements

- The pipeline is modular enough to audit one step at a time.
- Outputs are written as reports, CSVs, JSON, logs, plots, and HTML mirrors.
- The model-rule code keeps EIS metrics out of model selection.
- Logs scrub local absolute paths where the runner supports it.

---

## Slide 3: Open Issues

- Full real-data reruns still need the external DIB dataset and EIS workbook.
- The package does not vendor every dependency.
- Code portability depends on path configuration and the correct Python environment.
- Scientific validity is not solved by code organization.

---

## Slide 4: Roadmap

- Keep scripts runnable from the full project repo.
- Add command-line arguments where paths are still hard-coded.
- Add stricter tests around SOC mapping and model-rule selection.
- Freeze a validation protocol before expanding results.
