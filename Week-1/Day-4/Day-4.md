# Day 4


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

<a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-1/CarPricePrediction.ipynb">Notebook</a>

<ol>
  <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-1/Day-2/Day-2.md">In Day 2:</a>
    <li>Data preparation</li>
    <li>Exploratory Data Analysis (EDA)</li>
    <li>Setting up the validation framework</li>
  <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-1/Day-3/Day-3.md">In Day 3:</a>
  <li><a href="#4-linear-regression">Linear Regression</a></li>
  Continuation:
  <li><a href="#5-evaluating-the-model-with-rmse">Evaluating the model with RMSE</a></li>
  <li><a href="#6-simple-feature-engineering">Simple Feature Engineering</a></li>
</ol>

## 5. Evaluating the model with RMSE
RMSE is a way to evaluate regression models. It is a commonly used error metric for numerical predictions.

- First the **residuals** (the difference between the predicted value and the actual value) are squared. 
- Then, the **average of the residuals** is calculated by summing up all the squared residuals and dividing by the number of observations. (We call it Mean Squared Error in this step)
- Finally find the **square root of the average of the residuals** to find the RMSE.

It can range from 0 to ∞. The closer the RMSE to 0 the better, since it measures how spread out (standard deviation) the residuals are and the further the distance between the predicted value and the actual value, the bigger the RMSE.

Since the errors are squared before they are averaged, the RMSE gives a relatively high weight to large errors. This means the RMSE is most useful when large errors are unwanted.

![image](https://user-images.githubusercontent.com/70928356/192907565-5ad59ec6-0ede-400d-9c52-bdaf27fa7a04.png)

Where
- $g(x_i)$ -> prediction for xi
- $y_i$ -> actual value
- $m$ is the number of observations (e.g # of cars)

![image](https://user-images.githubusercontent.com/70928356/192906999-46cb6e23-0707-4b39-8d0e-b26595d136ea.png)

## 6. Simple Feature Engineering

### Categorical Data

There can sometimes be categorical data that consists of integers, such as number of doors. This is considered categorical since the values are discrete and not contiuous (e.g. can be 2, 3, 4 and not 2.5).

The way to represent a categorical column such as `number_of_doors` is as multiple binary columns.
- Find the unique values in that column.
- Create a new binary column for each of the unique value

![image](https://user-images.githubusercontent.com/70928356/193014657-087b897b-22f7-4e3a-ae70-b519ec8e15d0.png)

## Years

If there is a column such as `years` which contain the year a car was made, it can be better to turn it to `age` to find the age of the car.
