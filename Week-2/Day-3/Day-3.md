# Week 2 - Day 3

# Deploying Machine Learning Models

## Table of Contents

<ol>
  <li><a href="#1-saving-and-loading-the-model">Saving and loading the model</a></li>
</ol>

## 1. Saving and loading the model

### Saving the model
We will use `pickle` to save, which is a built-in library for saving Python objects.
- Install and import pickle
- Create a variable that has **name_of_model.bin**. This will be the output file: <br> `output_file = 'model.bin'`
- Save the model in output file using `pickle.dump`:
```python
    with open(output_file, 'wb') as f_out: # wb: write binary
      pickle.dump((dv, model), f_out) # dv: DictVectorizer, since we will need it in this model
```

### Loading the model
- Import pickle
-`model_file = 'model.bin'`, which is the name of the file that has the model. We want to load this file.
- Load the model using `pickle.load`:
``` python
with open(model_file, 'rb') as f_in:
  dv, model = pickle.load(f_in)
```

### Turn notebook into Python script
Download as `.py` file

## 2. Web Services: Introduction to Flask
### A simple ping pong app
