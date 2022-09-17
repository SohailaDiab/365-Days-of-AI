#### *17th September 2022*
# Day 2


## **Car Price Prediction**
How can we help a user select the best price for their car?

## Project plan
- Prepare data and do EDA (Exploratory Data Analysis)
- Use linear regression for predicting price
- Understand the internals of linear regression
- Evaluating the model with RMSE
- Feature engineering
- Regularization
- Using the model

**Notebook:**

### 1. Data preparation
- Change the column names to all lowercase and replace spaces with underscores
- Change the string values to all lowercase and replace spaces with underscores

This helps with consistency and dealing with data.

❌ Will not work to access the column:
```python
df.Transmission Type
```

✔ Will work to access the column:
```python
df.transmission_type
```
