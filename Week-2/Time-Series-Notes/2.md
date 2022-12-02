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

![image](https://user-images.githubusercontent.com/70928356/201738003-8bf9866e-4672-4546-b59e-4ed804c0fad3.png)

## What is Random Walk?
It is a special type of time series where values tend to persist over time and the differences between periods are simply white noise.

![image](https://user-images.githubusercontent.com/70928356/201738183-298b1951-a1ed-4cb2-a8ae-d4088b880e02.png)


## Market Efficiency
Measures the level of difficulty in forecasting correct future values.

In general, if a time series resembles a random walk, the prices can't be predicted with great accuract.

Conversely, if future prices can be predicted with great accuracy, then there are arbitrage opportunities. We can speak of arbitrage when investors managed to buy and sell commodities and make a safe profit, while the price adjusts.

## Stationarity
Time series stationarity implies that taking consecutive samples of data with the same size should have identical covariences regardless of the starting point.

This characteristic of the data is also known as **weak form** stationarity or **covariance** stationarity.

In order to consider a time-series as covariance stationarity it should have:
- A constant mean `µ`
- A constant variance `σ2`
- Consistent co variance between periods at an identical distance from one another `Cov(xn, xn+k) = Cov(xm, xm+k)`

Example of weak form stationary process is white noise.

**Note: WIP...**
