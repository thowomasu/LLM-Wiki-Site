# LG M50T 21700 Expt 4 drive-cycle aging Time-Series DRT Pipeline, EIS DRT baseline

## Purpose

This section fits every accepted GITT pulse in each 25-pulse processed file, then aggregates those pulse fits by file and SOC/pulse index.

## Results

- Files requested: 40
- Files completed: 40
- Files errored: 0
- Pulse fits completed: 1000
- Median fitted pulses per file: 25.0
- Median RMSE: 1.611414006136459 mV
- SOC bucket counts: `{"high_soc": 320, "low_soc": 320, "mid_soc": 360}`

## Outputs

- `section_5_gitt_pulse_fit_results.csv`: one row per accepted fitted pulse.
- `section_5_gitt_pulse_index_aggregate.csv`: aggregate pulse-index/SOC-proxy behavior across files.
- `section_5_gitt_batch_results.csv`: one row per file/RPT, now aggregated from all fitted accepted pulses.

## Interpretation

This is a cleaner engineering basis than one selected pulse per file.
The SOC values are ordered-pulse proxies, not measured SOC labels. Do not pretend otherwise.
The batch still lacks an EIS-derived DRT comparison target, so these are DRT-like health features, not validated DRT physics.
