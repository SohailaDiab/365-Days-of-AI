#### *16th September 2022*
# Day 1

### Table of Contents
  
<ol>
    <li><a href="#1-introduction-to-machine-learning">Introduction to Machine Learning</a></li>
    <li><a href="2-#machine-learning-vs-rule-based-systems">Machine Learning vs Rule-based Systems</a></li>
    <li><a href="#3-supervised-machine-learning">Supervised Machine Learning</a></li>
    <li><a href="#4-crisp-dm-ml-process">CRISP-DM ML Process</a></li>
    <li><a href="#5-model-selection">Model Selection</a></li>
  </ol>


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

![image](https://user-images.githubusercontent.com/70928356/190270146-91096fb2-0974-4676-86db-e98892ca8136.png)

### Types of Supervised ML tasks
1. **Regression**

Predict a target numerical value *(like price)* given a set of features *(like age, size, etc.)* called predictors.
The output is an **infinte set of numbers**.

Example:
Predict car price given its characteristics like age, brand, fuel type, etc.

2. **Classification**

A ML algorithm is required to learn how to assign a class label from the given domain. Target value is a finite set of categories. 

**_Multiclass classification:_**  
  Classify something into multiple different categories.
  Example: Classify an image into cars, cats or dogs.

**_Binary classification:_**  
  Classify something into 2 classes (0 or 1).
  Example: Classify emails into spam or not spam.
  
3. **Ranking**
 Usually used in cases when you want to rank something; a recommender system for example.
 
Example: A user goes to an e-commerce website. There is an algorithm that ranks the items from the probability that the user would like that item, and returns the top items (highest probability/score). Google also does the same thing by giving the most relevant websites based on the search.

## 4. CRISP-DM ML Process
Cross-Industry Standard Process for Data Mining.
A methodology for how machine learning projects should be organized.

1. **Business understanding**

Identify and understand the problem to be solved, as well as understand how to measure the success of the project. The goal of the project has to be measurable.

An important question at this step: **Do we actually need ML?**

2. **Data understanding**

Analyze available data sources and if more data is needed.
What is learnt at this step may influence the initial understanding of the problem, so we can go back and revise what we did in the first step.

3. **Data preparation**

Transform the data in such a way so that it can be put into a ML algorithm.
- Clean the data
- Build the pipelines
- Convert data into tabular form

4. **Modeling**

Training the model. The actual machine learning happens here.
Sometimes, we may go back to data preparation to add new features or fix data issues.

5. **Evaluation**

Measure how well the model performs and solves the business problem.

6. **Deployment**

Often happens with evaluation; the way models are evaluated is usually through deployment.

- Online Evaluation: Evaluation of live users
- Roll the model to all users
- Proper monitoring
- Ensuring the quality and maintainability

**ML projects require continuous iterations through the whole process!**

![image](https://user-images.githubusercontent.com/70928356/190294398-9962b221-a709-4a49-b2e9-83201c6e64ef.png)

## 5. Model Selection

We try different models and our goal is to choose the best model.

Trying all the models and seeing which one has the highest accuracy sounds good to do. However, there is a problem with this approach.

This is called **multiple comparison problems**, where we perform the same comparison many times using different models and evaluate them against the same validation dataset. A model can get lucky at predicting a particular part of the dataset and get a very high accuracy, but when given another part of the dataset it can get a lower accuracy and vice versa. 

**To overcome this issue:**

We will split the data into train, validation and test.

First, we will train part of the dataset and then evaluate using different models in the validation set.
We will then pick the model with the highest accuracy and evaluate it using the test set.

![image](https://user-images.githubusercontent.com/70928356/190409146-704d537e-7adc-4618-855a-b49b0fb8d53d.png)

1. Split
2. Train
3. Validate using different models *(re iterate throught steps 2 and 3 as much as we need)*
4. Select the best model
5. Use the best model selected on the test data
6. Check if the test accuracy is good
