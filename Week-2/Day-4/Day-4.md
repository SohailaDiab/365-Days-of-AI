# Time Series Analysis with Python

## What is white noise?
It is a special type of time-series, where the data does not follow a pattern. Therefore, it is unpredictable.

In order to consider a time-series as white noise it should have:
- A constant mean `µ`
- A constant variance `σ2`
- No autocorrelation in any period `p = corr(xt, xt-1)
  - Auto correlation measures how correlated a series is with past versions of itself
  - There is no clear relationship between past and present values of a time-series

Thus, white noise is a sequence of random data, where every value has a time-period associated with it.
