# Week 2 - Day 1

## Evaluation Metrics for Classification
Continuing on the Churn Prediction Example

## Table of Contents
All that is explained here is implemented in this <a href="">Notebook</a>.

<ol>
  <li><a href="#1-accuracy">Accuracy</a></li>
  <li><a href="#9-">Confusion Matrix</a></li>
  <li><a href="#9-">Precision and Recall</a>
    <ol>
        <li><a href="#what">Precision</li>
        <li><a href="#the-">Recall</li>
      </ol>
  </li>
</ol>

## 1. Accuracy
It is an evaluation metric for **classification** models.</br>
Accuracy measures the **fraction of correct predictions**. It is calculated by dividing the number of correct predictions by the total number of predictions.

### $Accuracy = {Correct  \ Predictions \over Total \ Predictions}$

- We can change the **decision threshold**, it should not be always 0.5. But, in this particular problem, the best decision cutoff, associated with the hightest accuracy (80%), was indeed 0.5. </br>
_(if probability of churning is above 0.5, consider that the customer will churn, otherwise will not churn)_

- Note that if we build a **dummy model** in which the **decision cutoff is 1**, so the algorithm predicts that **no clients will churn**, the accuracy would be 73%. Thus, we can see that the improvement of the original model with respect to the dummy model is not as high as we would expect.

- Therefore, in this problem **accuracy cannot tell us how good is the model** because the **dataset is unbalanced**, which means that there are more instances from one category than the other. This is also known as **class imbalance**.


