#### *14th September 2022*
# Day 1

## 1. Introduction to Machine Learning
### What is ML?
It is the science of programming computers so that they can learn from data:
- Learns from experience **E**
- On given tasks **T**
- And some performance measure **P**

*Performance on T as measured by P, improves with E*

Example:
Given a dataset containing the _features_ of cars (year, make, mileage, etc.) and a _target_ value (price), the machine learning model will learn the patterns in the data. We can then use this model to predict the prices of cars which we don't know, given that we have its features.

Training the model:
![image](https://user-images.githubusercontent.com/70928356/190253477-92eb94f8-4c81-47aa-bd89-64c8096f3060.png)

Making predictions:
![image](https://user-images.githubusercontent.com/70928356/190253766-33e86a8a-bb63-4f1b-8bec-e31985fd1fa7.png)


So generally speaking, machine learning is the process of extracting patterns from data. Data is usually of 2 types: features (info about the object) and target (what we want to predict).

A model encapsulates all the patterns it learned from the data.

### Types of ML Systems
**Trained with human supervision or not:**
- Supervised
- Unsupervised
- Semi-supervised
- Reinforcement

**Can learn incrementally on the fly or not:**
- Online
- Batch

**Work by comparing new data points to known data points, or by detecting patterns in the training data and building a predictive model:**
- Instance-based
- Model-based

## 2. Machine Learning vs Rule-Based Systems
Let's take an email system for example, where there is a **spam filter**. 
This can be done by trying to notice patterns that we find in the spam emails, such as if the email consists of "deposit" or the sender is "promotions@online.com" we mark it as spam, otherwise mark it as "good email". This can be done using hard code and _if statements_.

The issue here is that the spam emails change over time, and every time it changes we need to update the code and add more and more if statements. This will be a never-ending process and the code will be very difficult to maintain for the developer and will be prone to errors.

This is where machine learning comes in. We can take all the emails users have marked as spam as well as emails that are not spam and use them to train the machine learning model. This trained model will then be able to classify if an email is spam or not. The predictions are probabilities, and to make a decision it is necessary to define a threshold to classify emails as spam or not.

## 3. Supervised Machine Learning
Supervised ML is training the algorithm using labelled data to be able to classify data or predict outcomes accurately. The spam prediction example is SML since the model is trained using the features and target (output) values.
