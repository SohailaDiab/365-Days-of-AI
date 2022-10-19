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
