# CALCE Storage 25 C External Validation Manifest

## Scope

This is dataset qualification only. It does not validate the frozen CALB rule.

The script inspected only the five requested Storage archives and did not bulk-extract them.

## Input

- CALCE folder: `[local path redacted]`
- Archives inspected:
  - `PLN_Number_SOC_Temp_StoragePeriod.zip`
  - `Capacity Characterization_Initialization.zip`
  - `Impedance Characterization_Initialization.zip`
  - `Capacity_25C.zip`
  - `Impedance_25C.zip`

## Coverage

- PLN metadata rows: 150
- Capacity channel rows: 295
- Mapped capacity channel rows: 294
- Impedance CSV files: 282
- Same-PLN capacity plus EIS pairing rows: 24
- 25 C candidate PLN IDs: PLN45, PLN46, PLN47, PLN48, PLN51, PLN52, PLN53, PLN54, PLN59, PLN63, PLN64, PLN65, PLN67, PLN68, PLN69, PLN70, PLN71, PLN72, PLN73, PLN74, PLN75, PLN76, PLN77, PLN78

## Blunt Read

CALCE Storage 25 C is the better first external target for the frozen CALB rule qualification. It has explicit PLN IDs, SOC labels, 25 C storage conditions, capacity workbooks, and same-cell impedance CSVs. The cost is that it is storage/calendar ageing, not drive-cycle validation.

The CALCE adapter freezes 24 ready rows using `pln_id`, `temperature_c`, `storage_period`, and `soc_percent`. The frozen input build keeps all 24 as same-join qualification rows, but the current inputs expose 0 frozen pulse-to-EIS rule runnable rows because HPPC-compatible pulse windows are missing. That is blocked validation readiness, not external validation.

KIT/RADAR4KIT is second only after the corrected EIS addendum is available. NASA is still useful later, but it is the weaker target because its same-cell time-domain side is ordinary charge/discharge cycling. That is too far from the CALB pulse/drive-profile failure mode we already exposed.

## Outputs

- `zip_listing.csv`
- `pln_metadata.csv`
- `capacity_workbook_channels.csv`
- `impedance_csv_manifest.csv`
- `candidate_pairings.csv`
- `summary.json`
- `03_Adapter/adapter_candidate_table.csv`
- `03_Adapter/adapter_summary.json`
- `03_Adapter/README.md`
- `04_Frozen_Inputs/calce_storage_25c_frozen_input_rows.csv`
- `04_Frozen_Inputs/calce_storage_25c_frozen_input_summary.json`
- `05_Frozen_Rule_Run/calce_storage_25c_frozen_rule_summary.json`
- `06_Baseline_Comparison/calce_storage_25c_baseline_summary.json`
- `07_Validation_Report/calce_storage_25c_validation_summary.json`
