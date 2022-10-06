# Day 7

## **Churn Prediction - Classification**
We will use logistic regression to predict churn. 


## Table of contents
<a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-1/ChurnPrediction.ipynb">Notebook</a>

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
  <li><a href="#9-logistic-regression">Logistic Regression</a></li>
</ol>

## 8. One-hot encoding

### What is one-hot encoding?
It is a technique used to quantify categorical data that are not oridinal, we convert a categorical variable into a bunch of binary variables.
<br/>
*p.s. Ordinal means that the values are not ranked and are all of the same importance.*

**Let's take talk about an example to better understand this:**
<br/>
Say, we have a categorical variable called "Color", which consists of red, yellow and green. 

To apply one-hot encoding, each unique color in the "Color" column will have its own column that has only binary values (0 and 1). In this case, there will be 3 columns: "Red", "Yellow" and "Green".

For each record (row), depending on the color in the "Color" variable, we will assign a 1 to the column that represent that color and 0 to the rest of the columns. 
In the first record shown in the picture below, the color is red. Therefore, the first record of the "Red" column will have the value of 1, and the columns "Yellow" and "Green" will have the value of 0.

![image](https://user-images.githubusercontent.com/70928356/194159405-3a741d2e-100b-462c-836d-86d09cc8a292.png)

### Wy do we use one-hot encoding?
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
