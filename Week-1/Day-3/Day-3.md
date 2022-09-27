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

## 4. Linear Regression

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

## 4.1. Linear Regression: Vector form
Vector form of LR is the dot product between the feature matrix X and vector of weights w. The feature vector includes the bias term with an x value of 1.

![image](https://user-images.githubusercontent.com/70928356/192349796-47258f4c-487b-40d5-82dc-f51b96f321a8.png)

<a href="https://colab.research.google.com/drive/1_zlwG_QLW8IgOUGhL48HCfgT3MKCE8bs?usp=sharing">The code of this project</a>

## 4.2. Training Linear Regression: Normal Equation
`Xw = y`

How to solve for `w` if inverse for `X` exists:
`w = X^-1 y`

**Issue:**

This `X` is usually a rectangular matrix, so for that matrix the **inverse does not exist**.

**Solution:**

We can find an approximate solution for this by multiplying by the **transpose of X**, giving us the **Gram Matrix** `XT X`: 

![image](https://user-images.githubusercontent.com/70928356/192399301-5452c33f-4659-451a-82ce-4869079d42b5.png)

After that, we multiply by the inverse of the Gram Matrix:

![image](https://user-images.githubusercontent.com/70928356/192399513-b5c4d04f-1928-4884-951b-a4c768b09c76.png)


The Gram Matrix multiplied by its inverse becomes an identity matrix, so they cancel out:

![image](https://user-images.githubusercontent.com/70928356/192399581-a0b61b11-2208-4436-ae8f-3c0d0bca8997.png)

<a href="https://colab.research.google.com/drive/1_zlwG_QLW8IgOUGhL48HCfgT3MKCE8bs?usp=sharing">The code of this project</a>

