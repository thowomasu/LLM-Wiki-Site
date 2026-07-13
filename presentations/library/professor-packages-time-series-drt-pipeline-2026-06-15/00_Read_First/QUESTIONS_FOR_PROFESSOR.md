# Questions For Professor

These are the questions needed before this method can move from prototype to
credible validation.

## Protocol And Metadata

1. Which exact capacity-check pulse windows correspond to the EIS SOC labels
   of 95, 70, 50, 20, and 5 percent?
2. Is discharge current positive or negative in the DIB capacity CSV files?
3. Which time column should be considered authoritative: `Prog Time`, `Step
   Time`, or another protocol clock?
4. What measured capacity should be used for SOC reconstruction in each file?
5. Are the low-current pulse/rest windows intended to be comparable to
   small-signal EIS?

## EIS Reference

6. Which EIS preprocessing steps should be treated as reference?
7. Which DRT method and regularization setting were used in the prior thesis or
   reference workflow?
8. Should the comparison use raw gamma magnitude, normalized shape, broad-band
   areas, or another metric?

## Ground-Truth Validation Case

9. Can you provide one trusted matched example:
   cell, SOH, temperature, SOC, exact time-series pulse window, and matching EIS
   row?
10. What result would count as acceptable agreement for that trusted example?

## Main Risk To Review

The prototype reconstructs voltage well, but EIS agreement is weak. Please
review whether that mismatch is expected from protocol differences or whether it
points to a modeling flaw in the time-domain inverse.
