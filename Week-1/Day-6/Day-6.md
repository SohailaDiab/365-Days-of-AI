# Day 6

## **Churn Prediction - Classification**
We will use logistic regression to predict churn. 


## Table of contents
<a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-1/ChurnPrediction.ipynb">Notebook</a>

<ol>
  <li><a href="#1-business-understanding">Business Understanding</a></li>
  <li><a href="#2-data-preparation">Data Preparation</a></li>
  <li><a href="#3-setting-up-the-validation-framework">Setting Up the Validation Framework</a></li>
  <li><a href="#4-eda">EDA</a></li>
  <li><a href="#5-feature-importance-churn-rate-and-risk-ratio">Feature Importance: Churn Rate and Risk Ratio</a></li>
  <li><a href="#6-feature-importance-mutual-information">Feature Importance: Mutual Information</a></li>
  <li><a href="#6-feature-importance-correlation-coefficient">Feature Importance: Correlation Coefficient</a></li>
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

### **What is Risk Ratio?**

One of the feature importance metrics.

It is the ratio of the probability of an outcome in an exposed group to the probability of an outcome in an unexposed group. It is also known as **relative risk**.

To make it more clear, let's use churn as an example. In this case, the exposed group is the feature we want to analyze, for example, the `partner` feature. We want to see if having a partner makes a customer more likely to churn or not.

For that, the exposed group would be the churn rate of the `partner` feature (for each case, has partner or no partner), and the unexposed group would be the `global churn rate` (the churn rate for the whole dataset).

To calculate the risk ratio of customers that have a partner, we simply divide the churn rate of customers with a partner by the global churn. Same goes for customers with no partners.

To sum up: `Risk Ratio = cumulative incidence in the 'exposed' group / cumulative incidence in the 'unexposed' (global) group`.

![image](https://user-images.githubusercontent.com/70928356/193694966-b9445651-a7e8-4b15-8e84-3f0413b61c80.png)

![image](https://user-images.githubusercontent.com/70928356/193702615-eb096df6-dbb5-48ba-ada8-553e1fc972ef.png)


### Okay great, but how can we understand the value of the risk ratio?
Let's go back to the churn example:

- risk>1 : More likely to churn
- risk<1 : Less likely to churn

So if the risk is 1.22, then it means the churn rate is 22% higher (1.22-1) than the global churn rate. If the risk is 0.75, it means that the churn rate is 25% lower (1-0.75) than the global churn rate.


## 6. Feature Importance: Mutual Information
**What is Mutual Information?**

A way to measure the importance of categorical variables. It is concept from information theory. The Mutual Information between two random variables measures non-linear relations between them. Besides, it indicates how much information can be obtained from a random variable by observing another random variable.

**Example of the relationship we are interested in:**
- How much do we learn about churn if we observed the value of contract?
- If we know that a customer has a month-to-month contract, how much do we know about churn?

Mutual information is always larger than or equal to zero, where the larger the value, the greater the relationship between the two variables. If the calculated result is zero, then the variables are independent.

More info: https://quantdare.com/what-is-mutual-information/

## 6. Feature Importance: Correlation Coefficient
**What is Correlation Coefficient?**
It is a way to measrure how strong the relationship is between 2 variables. It can range from -1 to 1.

If negative, as value of x increases, value of y decreases (called negative correlation).

If positive, as value of x increases, value of y increases as well (called positive correlation).

- If a correlation is between **0.0 and 0.1**, it is considered a **very low correlation**. Meaning, and increase of one value **barely** leads to an increase of the other variable.

- If a correlation is between **0.2 and 0.5**, it is a **moderate correlation**. Meaning, the increase of the value of a variable **sometimes** leads to an increase of the other variable.

- If a correlation is between **0.6 and 1.0**, it is a **strong correlation**. Meaning, the increase of the value of a variable **often/always** leads to an increase of the other variable.

This goes for negative values as well.

![image](https://user-images.githubusercontent.com/70928356/193743065-84123bc5-be22-43fc-913f-08974175702c.png)

### Let's take an example for correlation between numerical variables and churn.

We have tenure (price customers pay monthly), which contains real numbers ranging from 0 to 72.

**Positive correlation:** More tenure leads to higher churn rate

**Negative correlation:** More tenure leads to lower churn rate

Zero correlation: Tenure has no effect on churn
