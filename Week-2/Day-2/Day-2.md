# Week 2 - Day 2

## Evaluation Metrics for Classification
Continuing on the Churn Prediction Example

## Table of Contents
All that is explained here is implemented in this <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-2/Evaluation_Metrics_for_Classification.ipynb">Notebook</a>.

<ol>
  <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-2/Day-1/Day-1.md">In Day 1:</a>
  <li>Accuracy</li>
  <li>Confusion Matrix</li>
  <li>Precision</li>
  <li>Recall</li>
  Continuation:
  <li><a href="#5-roc-curve">ROC Curve</a></li>
  <li><a href="#6-auc-roc-curve">AUC-ROC Curve</a></li>
  <li><a href="#7-cross-validation">Cross Validation</a></li>
</ol>

## 5. ROC Curve
ROC is Short for Receiver Operating Characteristic curve. It was originally used in WWII for evaluating the strength of radio detectors.</n>
It is a way of describing the performance of a binary classification model, and we can see how the model behaves at different thresholds.

This measure considers **False Positive Rate** (FPR) and **True Postive Rate** (TPR), which are derived from the values of the confusion matrix:

$True\ Positive \ Rate = \frac{ True \ Positive }{ True Positive + False Negative } $
</n>
- Look at all the actually positive examples (all the users who churned)
- Same as **Recall**
- **Maximize True Positive**

$False\ Positive \ Rate = \frac{ False \ Positive }{ False Positive + True Negative } $
</n>
- Look at all the actually negative examples (all the users who didn't churn)
- Fraction of False Positives
- **Minimize False Positive**

An ROC curve plots TPR vs. FPR at all the possible classification thresholds. Lowering the classification threshold classifies more items as positive, thus increasing both False Positives and True Positives. If the threshold is 0 or 1, the TPR and Recall scores are the opposite of the threshold (1 and 0 respectively), but they have different meanings, as we explained before.

![image](https://user-images.githubusercontent.com/70928356/196720835-643759d3-0e94-4290-8e44-4756a007ef55.png)

We need to compare the ROC curves against a point of reference to evaluate its performance, so the corresponding curves of random and ideal models are required. It is possible to plot the ROC curves with FPR and Recall scores vs thresholds, or FPR vs Recall.

**Classes and methods:**
- `np.repeat([x,y], [z,w])` - returns a numpy array with a z number of x values, and a w number of y values.
- `roc_curve(x, y)` - sklearn.metrics class for calculating the false positive rates, true positive rates, and thresholds, given a target x dataset and a predicted y dataset.

## 6. AUC-ROC Curve
One way of identifying how close we are to the ideal point (top left) in the ROC curve is measuring the **Area under the curve**.
</br>
The higher the AUC, the better the performance of the model at distinguishing between the positive and negative classes.

The AUC of an ideal model would be 1, and would be 0.5 for a random model.</br>
Since ROC is a curve of probability, AUC can be interpreted as the probability that a randomly selected positive example has a greater score than a randomly selected negative example.

![image](https://user-images.githubusercontent.com/70928356/196759906-efbec714-baf5-4540-a49f-596358c04889.png)

## 7. Cross Validation
We cannot simply say that the model is performing well because it predicted accurately on the training set, we need to also see if it **generalizes** well on unseen data. It is also important to see if the model is **stable** and performs almost similarly for different sets of data, and this is where Cross-Validation comes in, which is different from your usual train-test-split.

Splitting the data into train and test, usually 80%/20% or 70%/30%, etc. respectively, is called the **Hold-out** method. 

### What is Cross Validation?
It is a statistical method that allows us to estimate the performance of our ML model.
Cross-Validation allows us to compare different machine learning methods and get a sense of how they work in practice.

We will talk about **K-fold** cross validation.

So, what is K-Fold cross validation?
Instead of simply splitting the data to train and test set, we will split the data into **k-folds** (basically k parts) of equal sizes. We train on k-1 folds and validate on 1 fold

What you see in the image below is 5-fold cross validation, since here k=5. We divide the input data into 5 parts and use 4 parts for training and 1 part for validation.



![image](https://user-images.githubusercontent.com/70928356/196815046-1e459ace-f2a4-4928-99ce-3424b33b77fe.png)
