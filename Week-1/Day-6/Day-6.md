# Day 6

## **Churn Prediction - Classification**
We will use logistic regression to predict churn. 


## Table of contents
<a href="https://colab.research.google.com/drive/1s5r5xXtSXzCOJv-SPOhknk0kzBehS7sA?usp=sharing">Notebook</a>

<ol>
  <li><a href="#1-business-understanding">Business Understanding</a></li>
  <li><a href="#2-data-preparation">Data Preparation</a></li>
  <li><a href="#3-setting-up-the-validation-framework">Setting Up the Validation Framework</a></li>
  <li><a href="#4-eda">EDA</a></li>
  <li><a href="#5-feature-importance-churn-rate-and-risk-ratio">Feature Importance: Churn Rate and Risk Ratio</a></li>
</ol>

## 1. Business Understanding
**What is churn?**

The churn rate, also known as the rate of attrition or customer churn, is the rate at which customers stop doing business with an entity.

We need to predict if a customer in a Telecom company if they will churn or not, so that we will be able to retain that customer by offering discounts.

## 2. Data Preparation
- Change column names and values to lowercase and replace spaces with underscores make them consistent.
- Change incorrect column types:
  - `totalcharges` from object -> numeric
    - Tt will give an error since the original df had some empty values that changed to underscore when we swapped all spaces with underscores
    - To ignore such error and replace non-numerics with NaNs, use the `errors` parameter `pd.to_numeric(df.totalcharges, errors='coerce')`
    - Fill NaNs with 0s.
  - `churn` from object -> int 
    - yes to 1
    - no to 0

## 3. Setting Up the Validation Framework
- Split df to train/val/test
  - train: 60%
  - validation: 20%
  - test: 20%
- Get the target variables and delete the target variable from the features df

## 4. EDA
- Check missing values
- Look at target variable `churn`
- Look at numerical and categorical variables

## 5. Feature Importance: Churn Rate and Risk Ratio
