# Day 5 
More on evaluation metrics for regression.

### Table of Contents

<ol>
  <li><a href="#1-mean-absolute-error-mae">Mean Absolute Error (MAE)</a></li>
  <li><a href="#2-root-mean-squared-error-rmse-vs-mean-absolute-error-mae">Root Mean Squared Error (RMSE) vs. Mean Absolute Error (MAE)</a></li>
  <li><a href="#3-example-of-mae-and-rmse">Example of MAE and RMSE</a></li>
</ol>

## 1. Mean Absolute Error (MAE)

### First let's first recall what is Residual Error?
Residual error is the difference between the actual and predicted values.

### What is Mean Absolute Error (MAE)?
Another error metric that is very common to evaluate numerical predictions is Mean Absolute Error.

It is the sum of **absolute** differences between actual and predicted values (Residual errors). It ignores the direction of the error (i.e. +ve or -ve), so if the error is -15 we will take it as 15. 

If we take into account the direction, basically summing up the residual errors without finding the absolute, it is called Mean Bias Error (MBE).

Just like RMSE, MAE values can range from 0 to ∞ and the lower the value, the better a model fits a dataset.

![image](https://user-images.githubusercontent.com/70928356/193356543-e6e2ae73-8e91-4fc1-951b-694825b481ed.png)

## 2. Root Mean Squared Error (RMSE) vs. Mean Absolute Error (MAE)

### Similarities:
- The resulting values can range from 0 to ∞.
- The lower the value the more accurate the model is.

### Differences:
- RMSE is sensitive to outliers 
- RMSE penalizes large errors since the errors are squared
- MAE returns values that are more interpretable as it is simply the average of absolute error
- RMSE is always higher than or equal to MAE since the errors are squared. RMSE == MAE if all of the errors have the same magnitude

### When to use each?
- If you want to give more weights to observations that are further away from the mean, RMSE is more suitable when these large errors are unwanted since it gives a high weight to such errors.

**NOTE:**
- MAE can be defined as L1 loss.
- RMSE can be defined as L2 loss.

## 3. Example of MAE and RMSE
Let's say we are predicting heights, and these were the results of the actual height, the predicted height and the residual error (actual - predicted):

![image](https://user-images.githubusercontent.com/70928356/193364618-3db9458f-7bc0-423e-a5c1-982acea2b9f3.png)

### Let's find the Mean Absolute Error (MAE):
- First, we find the absolute of the residual errors 
- Next, sum up the absolute residual errors
- At last, to find the MAE we divide the sum by the number of observations 
  - Sum = 39
  - N obervations = 10
  - MAE = 39/10 = 3.9

![image](https://user-images.githubusercontent.com/70928356/193365043-dfae3b3f-69d5-41f6-87fe-6d8bf432ab8e.png)

> **Mean Absolute Error = 3.9**

### Now, let's find the Root Mean Squared Error (RMSE):
- First the residuals are squared
- Then, the squared residuals are summed up
- After that, we calculate the mean by dividing the sum of squared residuals by the number of observations (203/10 = 20.3)
- Finally find the square root of the average of the residuals to find the RMSE.

![image](https://user-images.githubusercontent.com/70928356/193365547-dae6c629-0cbf-447c-981f-15821ee9efc7.png)

> **Root Mean Squared Error = 4.506**

> We can see RMSE is always higher than MAE

### What would happen if there is an outlier?

**MAE:**

![image](https://user-images.githubusercontent.com/70928356/193366339-6da46e35-c993-479f-a67e-b4f160c83928.png)

**RMSE:**

![image](https://user-images.githubusercontent.com/70928356/193366367-ee4e6986-5122-4c1e-a790-fecefb5e99b2.png)

We can see a huge difference in the RMSE value!

While changed **MAE** from 3.9 to 8.5 **(only a 5.6 difference)**,
**RMSE** changed from 4.5 to 15.8 **(11.3 difference, more than double the MAE difference)**.

This was due to the fact that the residual error went from 2 to -48 in one of the observations, which resulted in the RMSE to increase significantly since it is sensitive to large errors.

