#### *20th September 2022*
# Day 3


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

### Table of Contents

<ol>
  <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-1/Day-2/Day-2.md">In Day 2:</a>
    <li>Data preparation</li>
    <li>Exploratory Data Analysis (EDA)</li>
    <li>Setting up the validation framework</li>
  Continuation:
  <li><a href="#4-linear-regression">Linear Regression</a></li>
</ol>

### 4. Linear Regression

Linear regression is a model that is used to solve **regression** problems.
We **input** to the model a `feature matrix X` and the **output** is a `vector y` containing the predictions.
The output of the model is a number.

``g(X) ≈ y``
* g-> Model *(Linear regression)*
* X -> Feature matrix 
* y -> Target vector

The LR formula is the sum of the `bias term w0` *(prediction we make without knowing anything about the features)* and each of the `feature values x` multiplied by their corresponding `weights w`.

``g(xi) = w0 + w1⋅xi1 + w2⋅xi2 + w3⋅xi3 + ...``

*compact form:*

![image](https://user-images.githubusercontent.com/70928356/191382236-19198e90-8d1b-4c32-90b5-9b17778750ea.png)
