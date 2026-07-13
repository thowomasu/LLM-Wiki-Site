# Drive-Cycle Dataset Recommendation

Prepared: 2026-06-15

## Blunt Decision

Do not defend DIB as the main dataset if the project requirement is drive-cycle battery behavior.

DIB is useful for the current prototype because it has pulse/rest capacity-check files and EIS rows. But that is not the same thing as a battery being run under a real drive-cycle profile. If the professor wants drive-cycle loading, DIB is the wrong main dataset.

## What A Drive-Cycle Dataset Needs

Minimum columns:

- time in seconds
- current in amps
- voltage in volts
- temperature in C, strongly preferred
- SOC label or enough information for coulomb counting
- cell chemistry and capacity
- named drive-cycle profile, for example FUDS, US06, UDDS, HWFET, LA92, WLTP, DST, or BJDST

Nice to have:

- repeated cycles over aging
- SOH labels
- impedance or EIS data
- multiple temperatures
- multiple cells

The hard truth: datasets with drive cycles plus clean matching EIS are harder to find. If the professor requires both, the project scope is bigger than the current package.

## Best Immediate Replacement: CALCE Battery Data

Use the CALCE battery data page first: [CALCE Battery Data](https://calce.umd.edu/battery-data).

Why this is the best first choice:

- CALCE says it provides open access lithium-ion test data including dynamic driving profiles, OCV measurements, impedance measurements, multiple form factors, and LCO, LFP, and NMC chemistries: [CALCE Battery Data](https://calce.umd.edu/battery-data).
- For the INR 18650-20R battery, CALCE lists dynamic current profiles including DST, FUDS, US06, and BJDST, tested at 80 percent and 50 percent battery level and at 0 C, 25 C, and 45 C: [CALCE dynamic test profile section](https://calce.umd.edu/battery-data).
- For the A123 battery, CALCE says the dynamic profile files contain DST, US06, and FUDS measurements, and the page lists temperature-specific downloads from -10 C to 50 C: [CALCE A123 dynamic profile section](https://calce.umd.edu/battery-data).

Recommended starting point:

1. Start with CALCE INR 18650-20R dynamic profiles at 25 C.
2. Use US06 and FUDS first.
3. Keep A123 as a second chemistry check if the project needs LFP behavior.

Why not start with A123? It is useful, but the 18650-20R page is closer to the common cylindrical EV-cell story and includes the named dynamic profiles clearly.

## What The Drive-Cycle Names Mean

The EPA page is useful for defining the profiles, even when the battery data comes from CALCE: [EPA Dynamometer Drive Schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules).

Key points from EPA:

- EPA says the page provides chassis dynamometer driving schedules and downloadable tab-delimited ASCII files used for emissions and fuel economy testing: [EPA drive schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules).
- UDDS represents city driving conditions: [EPA UDDS section](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules).
- HWFET represents highway driving under 60 mph: [EPA HWFET section](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules).
- US06 is a high-acceleration aggressive driving schedule: [EPA US06 section](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules).
- LA-92 is also listed as a heavy-duty driving schedule: [EPA LA-92 section](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules).

Use EPA to explain the drive-cycle profile. Use CALCE for actual battery current, voltage, and temperature data.

## Secondary Candidate: Panasonic 18650PF Drive-Cycle Data

There is a public Panasonic 18650PF drive-cycle dataset used in SOC-estimation literature, but I would not make it the first recommendation until the official download source is confirmed.

Why it is relevant:

- A 2020 NARXNN paper says the dataset used a Panasonic 18650PF cell and tested drive cycles including HWFET, LA92, US06, and UDDS at 25 C: [NARXNN paper](https://arxiv.org/abs/2012.10725).
- The same paper says the dataset contains voltage, current, temperature, and SOC information, and notes the current sensor error for the data collection: [NARXNN paper dataset section](https://arxiv.org/abs/2012.10725).
- A 2026 voltage-prediction paper also refers to a public Panasonic 18650PF dataset with UDDS, US06, LA92, and HWFET comparisons: [2026 paper](https://arxiv.org/abs/2605.06419).

Weakness:

The papers confirm the dataset is used, but the direct official dataset download was not cleanly verified from the search results I found. Do not tell the professor "we have this dataset" until the download path is confirmed.

## Dataset Choice

Use this decision rule:

| Requirement | Dataset Choice |
|---|---|
| Need named drive-cycle current profiles now | CALCE INR 18650-20R dynamic profiles |
| Need LFP chemistry | CALCE A123 dynamic profiles |
| Need HWFET, LA92, US06, UDDS in one SOC-estimation-style dataset | Panasonic 18650PF, but confirm official download first |
| Need drive-cycle definitions only | EPA drive schedule files |
| Need EIS-matched validation | DIB remains useful, but not as the drive-cycle dataset |

## How The Project Should Change

Use two tracks:

1. Drive-cycle track:
   - Use CALCE dynamic profiles.
   - Fit or test time-domain models on real dynamic current profiles.
   - Report voltage prediction, SOC behavior, thermal drift, and robustness.

2. EIS/DRT track:
   - Keep DIB only for pulse/rest plus EIS comparison.
   - Be honest that this is not the same as drive-cycle loading.

Do not mix the claims. That is the blind spot. If the dataset is pulse/rest, call it pulse/rest. If the dataset is drive-cycle, call it drive-cycle. The professor noticed the mismatch because it is real.

## Source List

- [CALCE Battery Data](https://calce.umd.edu/battery-data)
- [EPA Dynamometer Drive Schedules](https://www.epa.gov/vehicle-and-fuel-emissions-testing/dynamometer-drive-schedules)
- [Analysis of NARXNN for State of Charge Estimation for Li-ion Batteries on various Drive Cycles](https://arxiv.org/abs/2012.10725)
- [Residual-Corrected Equivalent-Circuit Model with Universal Differential Equations for Robust Battery Voltage Prediction under Operating-Condition Shift](https://arxiv.org/abs/2605.06419)
