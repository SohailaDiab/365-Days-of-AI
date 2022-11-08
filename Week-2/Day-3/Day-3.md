# Time Series Analysis with Python 

## What is Time-Series Data?
It is a sequence of information which attaches a time period to each value. <br>
The value can be anything measurable that depends on time in some way, such as prices, humidity, or number of people.

As long as the values we record are unambigous, any medium could be measured with time series. <br>
There aren't any limitations regarding the total time span of time series (could be min, day, month, etc.). <br>
All that is needed is a starting and ending point. Usually, there are many other points in between the start and end of a time series.

All time-periods must be equal and clearly defined, which would result in a constant frequency.

`Time period` : The intreval of time between recording one point of the set and the next.

`Frequency` : How often the values of the dataset are recorded.

All time-periods must be **equal and clearly defined**, which would result in a **constant** frequency. This is to be able to analyze time series in a meaningful way.

Patterns observed in time-series are expected to persist in the future. That is why we often try to predict the future by analyzing recorded values.

`Seasonality` : A characteristic of a time series in which the data experiences regular and predictable changes that recur every calendar year. Any predictable fluctuation or pattern that recurs or repeats over a one-year period is said to be seasonal.

### Examples:
- Meteorologists often cope with the task of forecasting the weather for days ahead to make remotely accurate predictions on a consistent basis. They rely on analyzing past data. Needless to say, **if the data is not recorded chronologically, finding the correct pattern would be extremely difficult**.
- Predict if sales will decrease or increase in the future and determine the stability of financial markets and efficiency portfolios.
