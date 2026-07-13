# Time-Domain DRT Pilot, time-series 2D DRT surface

## Purpose

This section checks whether the bad matched comparison is mostly a scale problem or a shape problem.
A constant scale problem is fixable. A shape problem means the current pulse inverse is not measuring the same thing as EIS under these settings.

## Scale Diagnostics Across SOC

- Median best scale factor from time-domain gamma to EIS gamma: 0.626434
- Max/min scale factor spread across SOC: 8.73118

- SOC 95 percent: corr=-0.041728605962128525, area_ratio=8.794288096146374, best_scale=0.41207108720247965, normalized_rmse=0.8611733917460707
- SOC 70 percent: corr=0.12090836447803356, area_ratio=8.912056554950443, best_scale=0.6264339319971866, normalized_rmse=0.8752405573249663
- SOC 50 percent: corr=0.08483606676781906, area_ratio=9.628350135387949, best_scale=0.6083849705701996, normalized_rmse=0.8907744526776245
- SOC 20 percent: corr=0.1906626620015067, area_ratio=45.65624079548599, best_scale=3.5978656610800597, normalized_rmse=0.9041803137104273
- SOC 5 percent: corr=0.10918997059877432, area_ratio=37.78830508588405, best_scale=1.9782092518392322, normalized_rmse=1.0911942377900854

## 70 Percent SOC Time-Domain Lambda Sweep

- Best normalized-RMSE lambda: 3.0
- Best normalized RMSE: 0.25903051759106727
- Correlation at best lambda: 0.28079590683495254
- Voltage RMSE at best lambda: 1.437430808399452 mV

- lambda 1e-05: RMSE=1.437 mV, corr=0.11948353078367253, scale=0.6128915755986049, norm_RMSE=0.8852425398761499, nonzero_gamma=8
- lambda 3e-05: RMSE=1.437 mV, corr=0.11948539827126779, scale=0.6129094633046954, norm_RMSE=0.8852290660463757, nonzero_gamma=8
- lambda 0.0001: RMSE=1.437 mV, corr=0.11950645845248933, scale=0.6131111695577985, norm_RMSE=0.8850771819429571, nonzero_gamma=8
- lambda 0.0003: RMSE=1.437 mV, corr=0.11967858296371778, scale=0.6147583327679073, norm_RMSE=0.8838403205447547, nonzero_gamma=8
- lambda 0.001: RMSE=1.437 mV, corr=0.12090836447803331, scale=0.6264339319971894, norm_RMSE=0.8752405573249621, nonzero_gamma=8
- lambda 0.003: RMSE=1.437 mV, corr=0.1749446680911015, scale=1.2491820965875584, norm_RMSE=0.5990603073061, nonzero_gamma=10
- lambda 0.01: RMSE=1.437 mV, corr=0.20988447575457825, scale=1.6965821771091385, norm_RMSE=0.5035329308285645, nonzero_gamma=14
- lambda 0.03: RMSE=1.437 mV, corr=0.26479419823245776, scale=2.4659007109119417, norm_RMSE=0.40053725786764693, nonzero_gamma=21
- lambda 0.1: RMSE=1.437 mV, corr=0.3382224869691008, scale=3.491950911777079, norm_RMSE=0.3165906653771042, nonzero_gamma=29
- lambda 0.3: RMSE=1.437 mV, corr=0.3528753676331177, scale=3.760944703753554, norm_RMSE=0.29739601019396156, nonzero_gamma=38
- lambda 1.0: RMSE=1.437 mV, corr=0.3179777796545447, scale=3.737078075035497, norm_RMSE=0.2871565107941499, nonzero_gamma=45
- lambda 3.0: RMSE=1.437 mV, corr=0.28079590683495254, scale=3.991221647645118, norm_RMSE=0.25903051759106727, nonzero_gamma=56

## Interpretation

If scale factors are not roughly constant across SOC, this is not just a missing unit conversion.
If lambda changes voltage RMSE but does not materially improve normalized shape agreement, then regularization alone is not the main fix.

Blunt takeaway: this section is designed to kill the lazy explanation. If the mismatch survives best scaling and lambda sweep, the next target is the model assumptions: SOC alignment, baseline/OCV handling, pulse excitation limits, and whether the EIS and pulse protocols are truly comparable.

<!-- BEGIN BEGINNER_MATH_EXPLANATION -->
## How This Section Works, Plain Math

This section asks whether the mismatch is only a scaling issue or a real shape issue.

### Scale test

If time-domain gamma is correct but too small, one scale factor should fix most cases.

The code checks:

```text
best scale = number that best maps time-domain gamma onto EIS gamma
```

If the best scale changes a lot by SOC, then the mismatch is not just one unit-conversion mistake.

### Normalized RMSE

After scaling, the code measures remaining shape error:

```text
normalized RMSE = scaled error / size of EIS curve
```

This makes cases with different absolute gamma sizes easier to compare.

### Lambda sweep

The code also tests several lambda values. Lambda controls smoothness:

```text
small lambda = more flexible gamma
large lambda = smoother gamma
```

### What this section proves

It shows that smoothing affects EIS agreement, but smoothing cannot be chosen by looking at EIS after the fact. That would be biased.

### Actual Equations Used

The best single scale factor for matching time-domain gamma to EIS gamma is:

$$
s^*
=
\frac{\gamma_{\text{TD}}^\top\gamma_{\text{EIS}}}
{\gamma_{\text{TD}}^\top\gamma_{\text{TD}}}
$$

After scaling, the remaining shape error is:

$$
\mathrm{NRMSE}_{\text{scaled}}
=
\frac{\left\|s^*\gamma_{\text{TD}}-\gamma_{\text{EIS}}\right\|_2}
{\left\|\gamma_{\text{EIS}}\right\|_2}
$$

The lambda sweep repeats the same optimization at different smoothness levels:

$$
\min_{\gamma \ge 0}
\left\|V-\hat{V}\right\|_2^2
+ \lambda\left\|L\gamma\right\|_2^2
$$

If the best \(\lambda\) is chosen after checking EIS, the validation is biased. The report treats that as a sensitivity test, not as final proof.
<!-- END BEGINNER_MATH_EXPLANATION -->
