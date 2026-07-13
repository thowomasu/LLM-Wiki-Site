# LG M50T 21700 Expt 4 drive-cycle aging Time-Series DRT Pipeline, HPPC candidate fit

## Purpose

This section fits the time-domain DRT model to the best accepted GITT pulse/rest window from HPPC window finder.

## Results

- RMSE: 0.282 mV
- R0: 0.0275399 ohm
- Tau range: 0.2 to 435 s
- Top recovered peaks: `[{"tau_s": 44.84027669205974, "gamma_ohm": 0.007962807989804309}, {"tau_s": 227.43628686742406, "gamma_ohm": 0.004507490977217634}, {"tau_s": 253.43846018505087, "gamma_ohm": 0.004421721893289679}, {"tau_s": 40.2397727065717, "gamma_ohm": 0.003975629172133104}, {"tau_s": 4.143691908066363, "gamma_ohm": 0.0011254117430638318}, {"tau_s": 0.6579160101623993, "gamma_ohm": 0.0009518749025284338}]`

## Interpretation

This proves the existing time-domain DRT fitter can run on LG M50T 21700 Expt 4 drive-cycle aging processed GITT data.
It does not prove physical validity. A smooth DRT curve after a good voltage fit is still not EIS validation.
