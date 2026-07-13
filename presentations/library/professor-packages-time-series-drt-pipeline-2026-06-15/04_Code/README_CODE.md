# Code Notes

The scripts are copied here for review in their original relative layout:

```text
scripts/experiments/
```

They are not meant to make this package a fully standalone runnable repository.
The full run expects the original project layout plus the DIB data paths.

For a plain-language walkthrough of the important scripts, read:

```text
../01_Method_And_Math/CODE_WALKTHROUGH_FOR_PROFESSOR.md
```

For regenerated plot details, read:

```text
../03_Key_Plots/PLOT_GUIDE.md
```

Main entry points:

- `scripts/experiments/run_time_domain_rough_prototype.py`
- `scripts/experiments/time_domain_model_rule.py`
- `scripts/experiments/time_domain_viability_report.py`
- `scripts/experiments/time_domain_export_html.py`
- `scripts/experiments/time_domain_package_plots.py`
- `scripts/experiments/time_domain_regenerate_all_plots.py`
- `scripts/experiments/time_domain_explain_outputs.py`

The core solver is:

- `scripts/experiments/time_domain_drt_pilot.py`

The pulse/window and fit stages are:

- `scripts/experiments/time_domain_window_finder.py`
- `scripts/experiments/time_domain_candidate_fit.py`

The batch and sensitivity stages are:

- `scripts/experiments/time_domain_dib_batch.py`
- `scripts/experiments/time_domain_soc_mapping_sensitivity.py`
- `scripts/experiments/time_domain_model_sensitivity.py`
