#### *17th September 2022*
# Day 2


## **Car Price Prediction**
How can we help a user select the best price for their car?

## Project plan
- Prepare data and do EDA (Exploratory Data Analysis)
- Use linear regression for predicting price
- Understand the internals of linear regression
- Evaluating the model with RMSE
- Feature engineering
- Regularization
- Using the model

**Notebook:**

### 1. Data preparation
- Change the column names to all lowercase and replace spaces with underscores
- Change the string values to all lowercase and replace spaces with underscores

This helps with consistency and dealing with data.

❌ Will not work to access the column:
```python
df.Transmission Type
```

✔ Will work to access the column:
```python
df.transmission_type
```
### 2. Exploratory Data Analysis (EDA)
- Find the number of unique values for each column, as well as the first 5 unique values
- Find the distribution of ``mrsp`` (price) by plotting a histogram
  -   ![image](https://user-images.githubusercontent.com/70928356/190876437-55735ee3-1bee-4cb6-8678-fdf12b25482f.png)
     > This type of distribution is called **Long Tail Distribution**
     
     > This kind of distribution is not really good for ML (the tail will confuse the model)
     
     > To get rid of this long tail, we will apply logarithmic distribution to get more compact values
  -   **Logarithmic distribution:**
      -   Since we cannot apply the log function to 0 (will be undefined), we will add 1 to each value to be sure that there are no 0s.
          ```python 
              np.log([0+1, 1+1, 10+1, 1000+1, 100000+1])
              output: array([ 0. , 0.69314718, 2.39789527, 6.90875478, 11.51293546])
          ```
          A NumPy function adds 1s manually, called ```np.log1p()```
  - ![image](https://user-images.githubusercontent.com/70928356/190876668-7f69b071-ca60-45b0-b443-a003a6cfc987.png)
  > We can now see that the long tail is gone and values are more compact
