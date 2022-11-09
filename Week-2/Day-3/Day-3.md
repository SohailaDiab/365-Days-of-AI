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

## Notation
Time-series variables:

- `X` : A variable that changes over a period of time.
- `T` : Entire period covered by a time-series.
- `t` : A single period within the interval.

**Example:**

- X: Daily closing prices for 2008
- T: Entire year
- t: A single day
- X<sub>t</sub> = X<sub>date/time/year</sub>: Closing price at a specific day

## Peculiarities of Time-Series Data

### Missing Values
Intervals between different observations need to be identical. If this is not the case, it is usually due to **missing values <br>
Values between consecutive periods usually affect each other and this can stir tons of trouble. So we must find ways to handle these limitations.

### Adjusting Frequency
We can adjust a frequency of a dataset depending on the values we are interested in.

For example, if we have daily data but want to conduct a monthly analysis, we need to compute some average value of all the individual daily data values. In this case, by aggregating the data, we will try to determine the best way to describe each month.

### Increasing Frequency
Sometimes we have to increase the frequency. This leads to an **increase in the number of time periods within the interval**, and consequently to new time periods without any values assigned to them.

To analyze the data successfully we need to approximate or impute the missing values for these periods.

### Splitting Data
Unlike other types of data, time-series data must be in **chronological order**. Meaning, if we want to perform ML we cannot shuffle the data before splitting it into train and test sets.

What we do instead is pick a cut-off point. The period before the cut-off point is the training set and the period after the cut-off point is the testing set.

The testing set is considered the future data.
