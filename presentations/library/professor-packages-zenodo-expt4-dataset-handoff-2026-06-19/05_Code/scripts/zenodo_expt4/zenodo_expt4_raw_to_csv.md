# LG M50T 21700 degradation study, Expt 4 drive-cycle aging raw CSV converter

This pipeline converts BioLogic `.mpt` and `.mpr` files under:

```text
<local Experiment 4 root>\Raw Data
```

Outputs are written under:

```text
[local converted data not published]
```

The converter keeps the raw folder structure and names outputs as
`source_file.mpt.csv` or `source_file.mpr.csv`. That avoids overwriting files
when an `.mpt` and `.mpr` share the same stem.

## Commands

Use the active DRT-capable Python environment:

```powershell
python scripts\experiments\zenodo_expt4\zenodo_expt4_raw_to_csv.py --dry-run
```

Convert only `.mpt` files:

```powershell
python scripts\experiments\zenodo_expt4\zenodo_expt4_raw_to_csv.py --include mpt
```

Convert `.mpr` files:

```powershell
python scripts\experiments\zenodo_expt4\zenodo_expt4_raw_to_csv.py --include mpr
```

Convert a small test sample:

```powershell
python scripts\experiments\zenodo_expt4\zenodo_expt4_raw_to_csv.py --include mpr --sort size --limit 1 --force
```

Convert files whose path contains a string:

```powershell
python scripts\experiments\zenodo_expt4\zenodo_expt4_raw_to_csv.py --match RPT9 --include all
```

## Notes

- `.mpt` files are converted directly from tab-delimited EC-Lab text.
- `.mpr` files require `galvani`, installed locally under `.deps\experiment-converters`.
- Existing outputs are skipped unless `--force` is passed.
- Each run writes `conversion_manifest.csv` and `conversion_manifest.json`.
- Full `.mpr` conversion can be slow and memory-heavy. Some raw files are over 1 GB.
