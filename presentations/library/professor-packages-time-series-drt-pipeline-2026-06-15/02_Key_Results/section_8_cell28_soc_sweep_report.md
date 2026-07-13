# Time-Domain DRT Pilot, combined EIS and time-domain DRT prototype

## Purpose

This section repeats the matched-pair comparison across Cell28 SOC points using the lower-current pulse windows.
The goal is not to declare success. The goal is to see whether the comparison behaves consistently enough to deserve more work.

## Cases

- SOC 95 percent, candidate 6, pre-rest V 4.1647, RMSE 1.492 mV, corr -0.04172860596212766, time area 0.0013867039131956322, EIS area 0.012195073716696127
- SOC 70 percent, candidate 10, pre-rest V 4.0106, RMSE 1.437 mV, corr 0.12090836447803378, time area 0.001912685167764021, EIS area 0.01704595838692804
- SOC 50 percent, candidate 14, pre-rest V 3.7029, RMSE 1.427 mV, corr 0.08483606676782145, time area 0.0012801401061692812, EIS area 0.012325637164550778
- SOC 20 percent, candidate 20, pre-rest V 3.4611, RMSE 1.493 mV, corr 0.19066266200150614, time area 0.0010519013202975173, EIS area 0.04802585997259331
- SOC 5 percent, candidate 24, pre-rest V 3.1803, RMSE 2.277 mV, corr 0.10918997059877449, time area 0.0018530087312008787, EIS area 0.07002205926142595

## Interpretation

This is the first real validation table. Treat it as a stress test.
If correlations and band areas jump around with no SOC pattern, the pipeline is still not validated.
If broad band trends are repeatable across SOC, then the next step is tuning regularization and reporting band-level features instead of peak-level claims.

Blunt warning: matching by pre-rest voltage is only an approximation. Proper validation needs exact SOC labels from the protocol or a capacity-integrated SOC estimate.

## Outputs

- `section_8_cell28_soc_sweep_summary.csv`
- `section_8_cell28_soc_sweep_summary.json`
- `section_8_cell28_soc_sweep_summary.png`

<!-- BEGIN BEGINNER_MATH_EXPLANATION -->
## How This Section Works, Plain Math

This section repeats the same fit-and-compare process across SOC labels.

### Why a sweep is better than one plot

One comparison can be lucky. A sweep asks whether the method behaves consistently across 95, 70, 50, 20, and 5 percent SOC.

For each SOC:

```text
1. choose a pulse window
2. fit time-domain DRT
3. compute EIS-derived DRT
4. compare both curves on shared tau
5. store voltage RMSE, correlation, and area
```

### What the metrics mean

Voltage RMSE says whether the local voltage fit is good.

Correlation says whether time-domain and EIS DRT shapes agree.

Area ratio says whether one curve has much more total resistance weight than the other.

### What this section proves

It gives repeatability evidence. In the current run, voltage fits are good, but EIS agreement is weak. That means the code is working mechanically, but the scientific method is not validated.

### Actual Equations Used

For each SOC label \(s\), the pipeline stores:

$$
\mathrm{RMSE}_{\mathrm{mV}}(s)
=1000\sqrt{\frac{1}{N_s}\sum_{n=1}^{N_s}
\left(V_{s,n}-\hat{V}_{s,n}\right)^2}
$$

The shape agreement with EIS is:

$$
r(s)=\operatorname{corr}
\left(\gamma_{\text{TD}}(\tau,s),\gamma_{\text{EIS}}(\tau,s)\right)
$$

The area ratio is:

$$
\rho_A(s)
=
\frac{\int \gamma_{\text{TD}}(\tau,s)\,d\log\tau}
{\int \gamma_{\text{EIS}}(\tau,s)\,d\log\tau}
$$

If voltage RMSE is low but \(r(s)\) is weak, the voltage fit is good but the DRT validation is weak.
<!-- END BEGINNER_MATH_EXPLANATION -->
