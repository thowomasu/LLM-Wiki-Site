# LG M50T 21700 Expt 4 drive-cycle aging Time-Series DRT Pipeline, time-series versus EIS 2D comparison

## Purpose

This section extracts health features from the 0.1C and 0.5C discharge curves.
These are not DRT inputs. They are capacity, voltage, current, and thermal ageing features.

## Results

- Files requested: 120
- Files completed: 120
- Files errored: 0
- Family counts: `{"0.1C Voltage Curves": 80, "0.5C Voltage Curves": 40}`

## Interpretation

This is the correct way to use constant-current discharge curves. They are strong SoH and capacity evidence, but weak DRT evidence.
Capacity-axis voltage features are target-conditioned for SOH/C10 checks, so the strict validation uses fixed-time voltage features instead.
