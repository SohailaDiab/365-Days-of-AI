#### *28th September 2022*
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
</ol>

## 5. Evaluating the model with RMSE
RMSE is a way to evaluate regression models. It is a commonly used error metric for numerical predictions.

- First the **residuals** (the difference between the predicted value and the actual value) are squared. 
- Then, the **average of the residuals** is calculated by summing up all the squared residuals and dividing by the number of observations. (We call it Mean Squared Error in this step)
- Finally find the **square root of the average of the residuals** to find the RMSE.

It can range from 0 to ∞. The closer the RMSE to 0 the better, since it measures how spread out the residuals are and the further the distance between the predicted value and the actual value, the bigger the RMSE.

Since the errors are squared before they are averaged, the RMSE gives a relatively high weight to large errors. This means the RMSE is most useful when large errors are unwanted.

![image](https://user-images.githubusercontent.com/70928356/192907565-5ad59ec6-0ede-400d-9c52-bdaf27fa7a04.png)

Where
- $g(x_i)$ -> prediction for xi
- $y_i$ -> actual value
- $m$ is the number of observations (e.g # of cars)



![image](https://user-images.githubusercontent.com/70928356/192906999-46cb6e23-0707-4b39-8d0e-b26595d136ea.png)

