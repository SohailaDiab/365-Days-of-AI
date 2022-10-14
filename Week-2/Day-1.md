# Week 2 - Day 1

## Evaluation Metrics for Classification
Continuing on the Churn Prediction Example

## Table of Contents
All that is explained here is implemented in this <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-2/Evaluation_Metrics_for_Classification.ipynb">Notebook</a>.

<ol>
  <li><a href="#1-accuracy">Accuracy</a></li>
  <li><a href="#2-confusion-matrix">Confusion Matrix</a></li>
  <li><a href="#3-precision">Precision</a></li>
  <li><a href="#4-recall">Recall</a></li>
</ol>

## 1. Accuracy
It is an evaluation metric for **classification** models.</br>
Accuracy measures the **fraction of correct predictions**. It is calculated by dividing the number of correct predictions by the total number of predictions.

### $Accuracy = {Correct  \ Predictions \over Total \ Predictions}$

- We can change the **decision threshold**, it should not be always 0.5. But, in this particular problem, the best decision cutoff, associated with the hightest accuracy (80%), was indeed 0.5. </br>
_(if probability of churning is above 0.5, consider that the customer will churn, otherwise will not churn)_

- Note that if we build a **dummy model** in which the **decision cutoff is 1**, so the algorithm predicts that **no clients will churn**, the accuracy would be 73%. Thus, we can see that the improvement of the original model with respect to the dummy model is not as high as we would expect.

- Therefore, in this problem **accuracy cannot tell us how good is the model** because the **dataset is unbalanced**, which means that there are more instances from one category than the other. This is also known as **class imbalance**.


## 2. Confusion Matrix

It is a way of measuring different errors the binary classification model makes.
</br>
We can get a better understanding of what kind of correct and incorrect decisions the model makes.

Considering this information, it is possible to evaluate the quality of the model by different strategies such as Precision, Recall, Accuracy, Specificity and AUC-ROC curves.

![image](https://user-images.githubusercontent.com/70928356/195854027-d677119f-8bc4-402b-8a86-7c9c3cb8ab70.png)

Let's take the churn prediction example, where the goal is to identify customers that will churn and send a promotional e-mail to them.

We have 2 target classes: Churn (1, positive class) and No Churn (0, negative class).</br>

- **TRUE POSITIVE (TP)** : 
Predicted positive and it was correct.</br>
_Predicted that the customer will churn, and they will actually churn._

- **TRUE NEGATIVE (TN)** : 
Predicted negative and it was correct.</br>
_Predicted that the customer will not churn, and they acutally won't churn._

- **FALSE POSITIVE (FP)** : 
Predicted positive and it was incorrect.</br>
_Predicted that the customer will churn, but they acutally won't churn._

- **FALSE NEGATIVE (FN)** : 
Predicted negatice and it was incorrect.</br>
_Predicted that the customer will not churn, but they actually will churn._

**Why we want to minimize False Positive and Negative:**</br>
For **False positives**, people would get the promotional email even though they weren't going to churn, therefore the company will lose money.

For **False negatives**, people that are going to churn will not receive a promotional email, making the company lose customers and profit.

> ℹ Accuracy is calculated as ${(TP + TN) \over (TP + TN + FP + FN)}$


## 3. Precision
It is the fraction of positive predictions that are correct. 

We predict that some customers are **churning**, and out of those we will get the ones that were **identified correctly**.

Here, we are only interested in the positive class (ones that we predicted will churn).

### $Precision = {True \ Positive  \over Total \ Positive \ Predictions} = {TP \over TP+FP}$

The higher the precision, the better.

Let's say that the result was 67%.</br>
This means that 33% of the people that received a promotional email were not going to churn and were not supposed to receive these emails.


## 4. Recall
It is the fraction of correctly identified positive observations, which in this example are the correctly identified churning users.

Here, we are only interested in the total actual positive observations.

### $Recall = {True \ Positive  \over Total \ Positive \ Observations} = {TP \over TP+FN}$

The higher the recall, the better.

Let's say that the result was 54%. </br>
This means that we failed to identify 46% of the people who will churn, which is not a good thing.
