# Plain English Overview

Prepared: 2026-06-15

## What This Package Is

This package is a research prototype. It tries to estimate a DRT-like relaxation curve from battery current, voltage, and time data. Then it compares that time-domain curve against an EIS-derived DRT curve when matching EIS data exists.

Plain version:

- Current goes into the battery.
- Voltage comes out of the battery.
- The code tries to explain the voltage response as a mix of fast, medium, and slow relaxation processes.
- Those relaxation processes are plotted over tau, which means time constant in seconds.
- The result is called DRT-like because it behaves like a DRT curve, but it is not validated as a true EIS replacement yet.

## What The Code Does

1. It creates a synthetic battery signal where the true answer is known.
2. It checks whether the solver can recover that known answer.
3. It loads battery CSV files and finds pulse/rest windows.
4. It fits one selected pulse/rest window.
5. It compares the fitted time-domain DRT against an EIS-derived DRT.
6. It repeats that comparison across SOC points and cells.
7. It tests whether SOC mapping, baseline choices, and lambda smoothing change the result.
8. It writes plots, CSV summaries, reports, and HTML copies.

## What The Plots Mean

- Current plots use amps, A.
- Voltage plots use volts, V.
- Voltage error plots use millivolts, mV.
- Tau plots use seconds on a log scale, because relaxation can happen over very different time ranges.
- Gamma or resistance-weight plots use Ohm or milliohm, mOhm.
- SOC plots use percent.
- Temperature drift uses C.

## What The Results Say

The engineering pipeline works. The code loads data, finds windows, fits curves, compares against EIS, and produces repeatable outputs.

The scientific claim is not proven. The EIS/time-domain DRT agreement is weak. The current rule-selected median EIS correlation is only about 0.141. That is too low to claim this is a valid EIS replacement.

The blunt version:

Do not train a model using these fitted DRT curves as final labels yet. That would be pretending the method is validated when it is not.

## The Main Weak Spots

1. The DIB data is not a clean drive-cycle dataset.
2. SOC matching is approximate, especially near the 70 percent case.
3. Baseline and lambda choices change the DRT comparison.
4. Good voltage reconstruction does not prove the recovered gamma shape is correct.
5. EIS and pulse/rest time-domain excitation may not be measuring the same process under the current assumptions.

## What To Ask In The Meeting

Ask these first:

1. Does the project require real drive-cycle profiles, such as FUDS, US06, UDDS, HWFET, or WLTP?
2. Is the goal SOC estimation, SOH estimation, EIS replacement, or DRT label generation?
3. Does the professor need drive-cycle data only, or drive-cycle data plus matching EIS?
4. Which current sign convention should be used?
5. Which exact SOC labels should be trusted?

If the answer is "we need drive cycles," then DIB should not be defended as the main dataset. Use DIB only for the EIS/pulse prototype, and switch the main experiment to a drive-cycle dataset.
