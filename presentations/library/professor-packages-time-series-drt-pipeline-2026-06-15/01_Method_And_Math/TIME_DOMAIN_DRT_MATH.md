# Time-Series To DRT Math

## Purpose

This document explains the math used by the current time-domain DRT prototype.

It is written for code review and research discussion, not publication.

Blunt warning: this is a DRT-like inverse model for pulse/rest time-series data. It is not a validated replacement for EIS-derived DRT.

The goal is to explain what the equations mean, how they map to the code, and where they can fool you.

## One-Screen Summary

The model tries to reconstruct measured terminal voltage from four pieces:

1. a free voltage baseline
2. an instantaneous ohmic term
3. many delayed RC-like relaxation terms
4. residual error

In compact form:

$$
v_n \approx b_n + R_0 i_n + \sum_{k=1}^{K}\gamma_k x_{k,n}
$$

The fitted DRT-like curve is the set of nonnegative weights:

$$
\gamma_1,\gamma_2,\ldots,\gamma_K
$$

Each gamma value says how much resistance the solver assigns to one relaxation time constant.

The dangerous part is that voltage reconstruction can be good even when the gamma distribution is wrong.

## Variables

| Symbol or Name | Unit | Meaning |
|---|---:|---|
| `n` | index | Time sample number inside one selected fit window. |
| `k` | index | Tau-grid index. One `k` means one virtual RC branch. |
| `t_n` or `time_s` | s | Time inside the selected window. The code resets each fit window to start at zero. |
| `i_n` or `current_a` | A | Measured current at sample `n`. The sign convention comes from the source CSV. |
| `v_n` or `voltage_v` | V | Measured terminal voltage at sample `n`. This is what the solver reconstructs. |
| `q_n` or `charge_as` | A s | Integrated current through time. Used as a local OCV drift proxy. |
| `R0` | ohm | Instantaneous ohmic resistance. It multiplies current directly. |
| `tau_k` or `tau_s` | s | Relaxation time constant for virtual RC branch `k`. |
| `x_{k,n}` | A | Current-like state of virtual RC branch `k` at sample `n`. |
| `gamma_k` or `gamma_ohm` | ohm | Nonnegative resistance weight assigned to `tau_k`. |
| `b_n` | V | Baseline voltage at sample `n`, including offset and optional drift terms. |
| `lambda_value` | local tuning value | Smoothness strength. Higher values punish jagged gamma curves more. |
| `D2` | matrix | Second-difference operator used to measure gamma curvature. |
| `A` | matrix | Nonnegative design matrix: current column plus RC-kernel columns. |
| `F` | matrix | Free baseline matrix: offset, charge drift, and/or time drift columns. |

## Step 1: The Fit Window

The solver does not fit the whole capacity CSV at once.

It first selects one pulse/rest window, then expands the slice to include rest before and after the pulse. In the batch runs, the real-data slice includes:

- 120 seconds before the pulse
- 1200 seconds after the pulse

The local time axis is reset:

$$
t_0 = 0
$$

This matters because the baseline and tau grid are local to one window, not global to the whole experiment.

## Step 2: Integrated Charge

The code computes integrated current using the trapezoid rule:

$$
q_0 = 0
$$

$$
q_n =
q_{n-1}
+
\frac{1}{2}
\left(t_n-t_{n-1}\right)
\left(i_n+i_{n-1}\right)
$$

Plain meaning:

- `q_n` is charge moved since the start of the selected window.
- It is measured in amp-seconds.
- It is not automatically true SOC.
- The model uses it as a local baseline/OCV drift clue.

The same idea is also used in SOC selection, after converting amp-seconds to amp-hours:

$$
Q_{\mathrm{Ah}} = \frac{q}{3600}
$$

Do not confuse local charge movement with ground-truth SOC. That would be sloppy.

## Step 3: Continuous-Time Idea

A current pulse creates two broad voltage effects:

- an immediate jump from ohmic resistance
- a delayed relaxation response from slower processes

The continuous-time idea is:

$$
v(t)
=
b(t)
+ R_0 i(t)
+ \int \gamma(\tau)x_{\tau}(t)\,d\log(\tau)
+ \varepsilon(t)
$$

Where:

- `b(t)` is baseline voltage.
- `R0 i(t)` is the instant ohmic voltage response.
- `x_tau(t)` is current passed through a virtual RC process with time constant `tau`.
- `gamma(tau)` says how much resistance is assigned to that time scale.
- `epsilon(t)` is whatever the model fails to explain.

The code does not solve the integral directly. It replaces the integral with a finite tau grid.

## Step 4: Discrete Forward Model

The code version is:

$$
v_n =
b_n
+ R_0 i_n
+ \sum_{k=1}^{K}\gamma_k x_{k,n}
+ \varepsilon_n
$$

Read this slowly:

- `v_n` is the measured voltage at one time sample.
- `b_n` is the free baseline at that sample.
- `R0 i_n` is the instant current-proportional voltage term.
- Each `x_{k,n}` is the current history filtered at one tau.
- Each `gamma_k` is the fitted resistance weight for that tau.
- The sum adds all delayed relaxation contributions.

Units check:

$$
\gamma_k x_{k,n}
=
\mathrm{ohm}\cdot\mathrm{amp}
=
\mathrm{volt}
$$

That is why `x` is current-like and `gamma` is resistance-like.

## Step 5: Virtual RC Branches

For each tau value, the hidden branch state obeys:

$$
\frac{d x_k(t)}{dt}
=
\frac{-x_k(t)+i(t)}{\tau_k}
$$

Plain meaning:

- `x_k` chases the measured current.
- If current stays constant, `x_k` slowly approaches that current.
- If current returns to zero, `x_k` decays back toward zero.
- Small tau follows current quickly.
- Large tau reacts slowly and keeps memory longer.

So each tau column is a different smoothed version of the current history.

## Step 6: Discrete RC Update

For sample `n`, define:

$$
\Delta t_n = t_n - t_{n-1}
$$

The code uses a trapezoidal, bilinear update:

$$
c_{k,n}
=
\frac{2\tau_k-\Delta t_n}{2\tau_k+\Delta t_n}
$$

$$
d_{k,n}
=
\frac{\Delta t_n}{2\tau_k+\Delta t_n}
$$

$$
x_{k,n}
=
c_{k,n}x_{k,n-1}
+ d_{k,n}(i_n+i_{n-1})
$$

What the pieces mean:

- `c` carries forward the previous RC state.
- `d` controls how much the current samples at both ends of the interval affect the new state.
- The update uses both `i_n` and `i_{n-1}`, so it is less crude than forward Euler.
- This is more stable when tau is close to the sample interval.

If `tau_k` is very small, the branch follows current quickly. If `tau_k` is very large, the branch moves slowly and remembers earlier current.

## Step 7: Kernel Matrix

After computing all virtual RC states, the code builds a kernel matrix:

$$
K_{n,k} = x_{k,n}
$$

Rows are time samples.

Columns are tau values.

Then the nonnegative design matrix is:

$$
A =
\begin{bmatrix}
i & K_{\tau_1} & K_{\tau_2} & \cdots & K_{\tau_K}
\end{bmatrix}
$$

The first column is measured current. Its coefficient is `R0`.

The remaining columns are RC-kernel columns. Their coefficients are gamma values.

So:

$$
A\theta
=
R_0 i
+ K\gamma
$$

Where:

$$
\theta =
\begin{bmatrix}
R_0 & \gamma_1 & \gamma_2 & \cdots & \gamma_K
\end{bmatrix}^{T}
$$

## Step 8: Tau Grid

The solver uses 72 tau values on a log-spaced grid.

The lower end is:

$$
\tau_{\min}
=
\max\left(2\,\mathrm{median}(\Delta t),10^{-3}\right)
$$

The upper end is:

$$
\tau_{\max}
=
\max\left(20\tau_{\min},\frac{T_{\mathrm{window}}}{3}\right)
$$

Where:

$$
T_{\mathrm{window}} = t_{N-1}-t_0
$$

Why this exists:

- `tau_min` needs more than one sample per relaxation.
- `tau_max` should stay tied to the visible window duration.
- A short window cannot honestly recover a very slow process.
- Log spacing gives coverage across fast, mid, and slow time scales.

If a recovered peak lands at the maximum tau boundary, treat it as suspicious. It often means the window is too short or the baseline is leaking into gamma.

## Step 9: Baseline Terms

The solver separates resistance terms from baseline terms.

Resistance terms are constrained nonnegative:

$$
\theta \ge 0
$$

Baseline terms are free to be positive or negative:

$$
Fz
$$

The full fitted voltage is:

$$
\widehat{v}
=
A\theta + Fz
$$

The baseline matrix `F` depends on `baseline_mode`.

### Offset Mode

$$
b_n = z_0
$$

This allows only a constant voltage offset.

### Time Mode

$$
b_n = z_0 + z_t(t_n-\overline{t})
$$

This allows a constant offset plus linear time drift.

### Charge Mode

$$
b_n = z_0 + z_q q_n
$$

This allows local OCV-like movement with charge throughput.

### Time-Charge Mode

$$
b_n
=
z_0
+ z_q q_n
+ z_t(t_n-\overline{t})
$$

This is the most flexible current first-pass baseline.

The baseline is not DRT resistance. It exists because terminal voltage can drift for reasons that are not relaxation resistance.

## Step 10: Smoothness Penalty

DRT inversion is ill-conditioned. Many gamma curves can fit almost the same voltage.

So the solver penalizes jagged gamma curves.

The second-difference operator is:

$$
(D_2\gamma)_j
=
\gamma_j - 2\gamma_{j+1} + \gamma_{j+2}
$$

If gamma bends sharply from one tau point to the next, this value is large.

If gamma is smooth, this value is small.

The smoothness penalty is:

$$
\lambda^2\left\|D_2\gamma\right\|_2^2
$$

Important:

- `R0` is not smoothed.
- Only the gamma vector is smoothed.
- Higher lambda makes gamma smoother.
- Smoother does not automatically mean more true.

## Step 11: Optimization Problem

The code solves:

$$
\min_{\theta,z}
\left\|A\theta + Fz - v\right\|_2^2
+
\lambda^2\left\|D_2\gamma\right\|_2^2
$$

Subject to:

$$
\theta \ge 0
$$

Where:

- `theta` contains `R0` and all gamma values.
- `z` contains free baseline coefficients.
- `A theta` is the nonnegative resistance part.
- `F z` is the free baseline part.
- `v` is measured voltage.
- `D2 gamma` measures gamma roughness.

The nonnegativity constraint means:

$$
R_0 \ge 0
$$

$$
\gamma_k \ge 0
\quad
\mathrm{for\ all}\ k
$$

This is physically motivated. Negative resistance weights would make the curve easier to fit, but harder to defend.

## Step 12: How The Solver Handles Free Baseline Terms

The active-set NNLS solver can handle nonnegative coefficients, but baseline terms must be allowed to go positive or negative.

So the implementation does this:

1. Project the voltage vector and nonnegative design matrix against the free baseline space `F`.
2. Solve the regularized nonnegative least-squares problem for `theta`.
3. Fit the free baseline coefficients `z` by ordinary least squares after `theta` is chosen.

In plain language:

- First remove what the baseline could explain.
- Fit nonnegative resistance terms to what is left.
- Then add the best baseline back.

This keeps gamma from being forced to explain every slow voltage movement.

## Step 13: Reconstructed Voltage And RMSE

After fitting, reconstructed voltage is:

$$
\widehat{v}
=
A\widehat{\theta}
+ F\widehat{z}
$$

Residual voltage is:

$$
r_n = v_n-\widehat{v}_n
$$

Voltage RMSE is:

$$
\mathrm{RMSE}_{V}
=
\sqrt{
\frac{1}{N}
\sum_{n=0}^{N-1}
\left(v_n-\widehat{v}_n\right)^2
}
$$

The reports usually show millivolts:

$$
\mathrm{RMSE}_{mV}
=
1000\,\mathrm{RMSE}_{V}
$$

Low RMSE is required. It is not enough.

A low RMSE only says the model can reconstruct terminal voltage. It does not prove the tau distribution is physically right.

## Step 14: Broad Tau Bands

Exact DRT peak locations are fragile, especially for pulse data.

So the reports also summarize broad tau bands:

| Band | Tau Range |
|---|---:|
| Fast | 4 to 16 s |
| Mid | 25 to 90 s |
| Slow | 90 to 450 s |

Each band is currently summarized by summing gamma values in that tau interval:

$$
G_{\mathrm{band}}
=
\sum_{\tau_k\in\mathrm{band}}\gamma_k
$$

This is not a final electrochemical feature. It is a stability diagnostic.

If the broad bands jump wildly when lambda changes slightly, the fitted gamma is fragile.

## Step 15: EIS Comparison

The time-domain fit gives:

$$
\gamma_{\mathrm{TD}}(\tau)
$$

The EIS pipeline gives:

$$
\gamma_{\mathrm{EIS}}(\tau)
$$

They usually do not share the exact same tau grid. The code compares only the overlap:

$$
\tau_{\mathrm{overlap,min}}
=
\max(\tau_{\mathrm{TD,min}},\tau_{\mathrm{EIS,min}})
$$

$$
\tau_{\mathrm{overlap,max}}
=
\min(\tau_{\mathrm{TD,max}},\tau_{\mathrm{EIS,max}})
$$

Then EIS gamma is interpolated onto the time-domain tau grid in log-tau space.

Correlation is computed over the overlap:

$$
\rho
=
\operatorname{corr}
\left(
\gamma_{\mathrm{TD}}(\tau),
\gamma_{\mathrm{EIS}}(\tau)
\right)
$$

What correlation means:

- High positive correlation means similar shape over shared tau.
- Near-zero correlation means weak shape agreement.
- Negative correlation means the curves move in opposite directions.

Correlation does not fix magnitude mismatch.

## Step 16: Area And Shape Metrics

The comparison also computes log-tau area:

$$
A_{\mathrm{TD}}
=
\int
\gamma_{\mathrm{TD}}(\tau)
\,d\log(\tau)
$$

$$
A_{\mathrm{EIS}}
=
\int
\gamma_{\mathrm{EIS}}(\tau)
\,d\log(\tau)
$$

The area ratio is:

$$
\frac{A_{\mathrm{EIS}}}{A_{\mathrm{TD}}}
$$

The code also asks:

What scale factor best maps the time-domain gamma curve onto the EIS gamma curve?

$$
s^*
=
\frac{
\gamma_{\mathrm{TD}}^{T}\gamma_{\mathrm{EIS}}
}{
\gamma_{\mathrm{TD}}^{T}\gamma_{\mathrm{TD}}
}
$$

Then scaled RMSE is:

$$
\mathrm{RMSE}_{\mathrm{scaled}}
=
\sqrt{
\frac{1}{M}
\sum_{m=1}^{M}
\left(
s^*\gamma_{\mathrm{TD},m}
-
\gamma_{\mathrm{EIS},m}
\right)^2
}
$$

The normalized RMSE compares shapes after area normalization:

$$
\mathrm{NRMSE}
=
\sqrt{
\frac{1}{M}
\sum_{m=1}^{M}
\left(
\frac{\gamma_{\mathrm{TD},m}}{|A_{\mathrm{TD}}|}
-
\frac{\gamma_{\mathrm{EIS},m}}{|A_{\mathrm{EIS}}|}
\right)^2
}
$$

Plain meaning:

- Correlation checks shape direction.
- Area ratio checks total gamma scale.
- Best scale checks whether one curve is mostly a scaled version of the other.
- Normalized RMSE checks shape mismatch after removing total area.

## Step 17: Model-Rule Selection

The sensitivity runs showed that lambda and baseline choices can change EIS agreement.

So the model-rule script chooses lambda before EIS scoring.

The current rule:

1. Fix `baseline_mode = time_charge`.
2. Fit the same window across a lambda grid.
3. Find the best voltage RMSE.
4. Keep lambdas within best RMSE plus max 5 percent or 0.25 mV.
5. Prefer lower gamma roughness.
6. Prefer stable fast/mid/slow band areas across neighboring lambdas.
7. Penalize edge lambda values and nearly flat gamma curves.
8. Only after lambda is selected, compare against EIS.

Gamma roughness is:

$$
\mathrm{roughness}
=
\frac{
\left\|\Delta^2\gamma\right\|_2
}{
\max\left(\left\|\gamma\right\|_2,10^{-15}\right)
}
$$

The selection score is rank-based in the code:

$$
\mathrm{score}
=
2r_{\mathrm{RMSE}}
+ r_{\mathrm{roughness}}
+ r_{\mathrm{band}}
+ p_{\mathrm{boundary}}
+ p_{\mathrm{flat}}
$$

Where:

- `r_RMSE` ranks voltage RMSE, lower is better.
- `r_roughness` ranks gamma roughness, lower is better.
- `r_band` ranks band instability, lower is better.
- `p_boundary` penalizes the smallest or largest tested lambda.
- `p_flat` penalizes gamma curves with too few nonzero points.

EIS correlation is not part of this score.

That is the point.

## Why Gamma Is Fragile

Gamma is fragile because this is an inverse problem.

Common failure modes:

- Many gamma curves can explain nearly the same voltage.
- Short windows cannot resolve long tau values.
- Baseline terms can compete with slow gamma.
- Strong smoothing can make curves look cleaner without making them truer.
- Weak smoothing can fit noise.
- EIS and pulse/rest data may not excite the same processes.
- SOC mismatch can compare the time-domain curve against the wrong EIS row.
- Temperature drift can move voltage for reasons unrelated to relaxation resistance.

That is why the pipeline reports more than one metric.

## What The Current Numbers Mean

The current viability report says:

- synthetic inverse check passes, RMSE about 0.801 mV
- DIB batch runner produces 15 rows with 0 errors
- SOC mapping sensitivity produces 60 comparisons with 0 errors
- model sensitivity produces 120 comparisons with 0 errors
- pre-declared model rule produces 10 selected comparisons with 0 errors

But the science is still weak:

- first DIB batch median EIS correlation is about 0.105
- pre-declared rule median EIS correlation is about 0.141
- pre-declared rule median normalized RMSE is about 0.978
- model sensitivity found 10 of 10 targets where correlation range changed by more than 0.1 across settings

Translation:

The code can fit voltage and generate curves. The recovered DRT shape is still too assumption-sensitive to call validated.

## What Would Make The Math More Defensible

The math gets stronger only if the assumptions get stronger.

Needed next steps:

- confirm protocol annotations tying pulse windows to SOC targets
- validate synthetic cases with known baseline drift, SOC drift, and temperature drift
- compare repeated pulse windows at the same condition
- improve OCV/baseline modeling
- choose lambda by a rule that survives new cells
- test the pre-declared rule on more cells and SOH labels
- report failures instead of tuning around them

Blunt version:

The math is good enough to investigate. It is not good enough to claim victory.
