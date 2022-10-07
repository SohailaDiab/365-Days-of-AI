# Day 7

## **Churn Prediction - Classification**
We will use logistic regression to predict churn. 


## Table of contents
All that is explained here is implemented in this <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-1/ChurnPrediction.ipynb">Notebook</a>.

<ol>
  <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-1/Day-6/Day-6.md">In Day 6:</a>
  <li>Business Understanding</li>
  <li>Data Preparation</li>
  <li>Setting Up the Validation Framework</li>
  <li>EDA</li>
  <li>Feature Importance: Churn Rate and Risk Ratio</li>
  <li>Feature Importance: Mutual Information</li>
  <li>Feature Importance: Correlation Coefficient</li>
  <b>Continuation:</b>
  <li><a href="#8-one-hot-encoding">One-hot Encoding</a></li>
  <li><a href="#9-logistic-regression">Logistic Regression</a>
    <ol>
      <li><a href="#what-is-logistic-regression">What is Logistic Regression?</li>
      <li><a href="#the-sigmoid-function">The Sigmoid Function</li>
    </ol>
  </li>
</ol>



## 8. One-hot encoding

### What is one-hot encoding?
It is a technique used to quantify categorical data. We convert a categorical variable into a bunch of binary variables.
<br/>

**Let's talk about an example to better understand this:**
<br/>
Say, we have a categorical variable called "Color", which consists of red, yellow and green. 

To apply one-hot encoding, each unique color in the "Color" column will have its own column that has only binary values (0 and 1). In this case, there will be 3 columns: "Red", "Yellow" and "Green".

For each record (row), depending on the color in the "Color" variable, we will assign a 1 to the column that represent that color and 0 to the rest of the columns. 
In the first record shown in the picture below, the color is red. Therefore, the first record of the "Red" column will have the value of 1, and the columns "Yellow" and "Green" will have the value of 0.

![image](https://user-images.githubusercontent.com/70928356/194159405-3a741d2e-100b-462c-836d-86d09cc8a292.png)

### Why do we use one-hot encoding?
Some ML algorithms can comprehend categorical variables, such as decision tree algorithm. However, many other algorithms cannot, and require the input to be numerical. This means that any categorical data must be mapped to integers.

We could simply just assign a number for each categorical variable, right? Like 1 for blue, 2 for red, etc. <br/>
**Well.. not really.** <br/>
This would cause an issue, since the model interprets larger numbers to have more importance; so if blue is represented as 1 and red as 2, it would consider red to be more important than blue.

Luckily, one-hot encoding solves this issue. Instead of representing categorical values as numbers ranging from 1-n, we will create multiple categorical columns for each unique value that are assigned a binary value of 0 or 1.

However, if the categorical variable is ordinal (meaning that the values can be ordered such as very high to very low), they can be handled in a different way such as Ordinal Encoding.

### How do we implement one-hot encoding?
***You can see the full implementation in the notebook.***

We make use of `DictVectorizer()`, which transforms lists of feature-value mappings to vectors 

1. Turn records into dictionary by using `df.to_dict(orient='records')`
2. Create a `DictVictorizer()` and set the `sparse` parameter to False.
3. Fit `DictVictorizer()` by passing to it the dictionaries
4. See what are the feature names by `dv.get_feature_names()`, which based on that it creates the feature matrix
5. Use `dv.transform(dicts)` to get the encoded matrix. This will be our X.

`DictVictorizer()` is smart enough to recognize numerical variables, and it leaves it as it is. So, there will be no issue with passing it numerical variables.

### Ever wondered why is it called one-hot encoding?
"Hot" means that the value is activated, and we activate it by representing it as a 1. Deactivated values are encoded as 0s.<br/>
It is called one-hot because only one bit is “hot” or TRUE at any time.

<br/>
You can read more about other techniques in categorical data encoding <a href="https://analyticsindiamag.com/a-complete-guide-to-categorical-data-encoding/">here</a>.

## 9. Logistic Regression

### What is Logistic Regression?
It is a supervised machine learning classification algorithm used to predict the probability of a binary target variable occurring.<br/>
Logstic Regression deals with **binary classification**. 

Target values can only be 0s and 1s:
<br/>
 - 1: Positive (churn)
 - 0: Negative (no churn)

g(xi) -> 0-1 (probability of xi belonging to the positive class)

The output is the probability of the positive target variable occuring. <br/>
Using the churn prediction example, if the output is 0.7, it means that there is a 70% chance that the customer will churn.

> It is very similar to linear regression, except that we have scores and we apply sigmoid function to it.<br/> Both linear and logistic regression are linear models. The reason they are called linear is because we they use the dot product (which is called linear operator in linear algebra).

### The Sigmoid Function

It is called **Logistic** regression since it makes use of the Logistic function, which is also called Sigmoid.

This function is used to map the predicted values to probabilities. We apply it on the score so that all the values are transformed into the range between 0 to 1.

**Formula:**

### $S(x) = {1 \over (1+e^(-x))}$

<br/>

```py
def logistic_regression(xi):
  score = w0

  for j in range(len(w)):
    score = score + xi[j]*w[j]

  result = sigmoid(score)
  return result
```
> We can see that the code above is very similar to Linear Regression; except, we have applied the Sigmoid Function.

![image](https://user-images.githubusercontent.com/70928356/194294354-c6500f6c-0cd5-485c-a3d5-d8d5d4272f93.png)

We have a threshold value, in which if the values cross it, we can classify the outcome as 1 (TRUE/positive). Otherwise, it will be classified as 0 (FALSE/negative).

In the image above, the treshold value is 0.5.<br/>
Let's go back again to the churn example. If the value is above 0.5, it means that the **customer will churn**, and if it is below 0.5, it means that the **customer will not churn**.
