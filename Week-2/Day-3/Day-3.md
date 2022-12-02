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

### What is a web service?
A web service is simply a software system that is specially designed to propagate communication between the client and server applications on WWW (World Wide Web). In simple words, it is the method of communication among two or more devices over a network.

<a href="https://www.w3schools.com/tags/ref_httpmethods.asp">About GET and POST methods</a>

### A simple ping pong app

![image](https://user-images.githubusercontent.com/70928356/205270303-6740e8b2-b847-4e30-b3e2-6b550a07d625.png)

Here: <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-2/Day-3/ping.py">ping.py</a>

- Run on cmd by typing `python ping.py`

![image](https://user-images.githubusercontent.com/70928356/205271990-e093fd2e-3710-4778-b4ae-88bc5104e660.png)

- Open another terminal and use curl `curl http://192.168.1.104:2020/ping` 

![image](https://user-images.githubusercontent.com/70928356/205272269-6812532e-d710-44de-83d5-0db9eaa572c0.png)

- OR you can view it on the web browser by typing `http://192.168.1.104:2020/ping` in the bar

## 3. Serving the Churn Model with Flask

![image](https://user-images.githubusercontent.com/70928356/205274457-1e59e274-4349-4d70-9342-8e5fe855e2f5.png)

Wrap the prediction script (Python file) into a flask app <br>
Here: <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-2/Day-3/predict.py">predict.py</a>

- If Flask is run in `DEBUG` mode, it reloads the server after every change to app file
```python 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=20303)
```

- Use POST method, since we want to send info about the customer
```python
app = Flask('churn')
@app.route('/predict', methods=['POST'])
```
- In the **predict** function, we take the body of the **request** as json, which contains the customer info we will use as features.
- Return the **response** also as a json. This contains the prediction.

**However, when we run this, we will get an error:**

![image](https://user-images.githubusercontent.com/70928356/205276787-ea412705-de73-4b22-80f8-e30601555281.png)

- This happens if we directly run predict.py since a browser is sending a GET request, but it says 405 meaning the method is not allowed.
- The allowed method is post, since in the predict.py file we typed `@app.route('/predict', methods=['POST'])`.
- We need to send a post request and from the browser it's not easy. So we will do it like this <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-2/Day-3/predict-test.ipynb">notebook</a> instead.

**We might also get response `500`**.
- This means that the server encountered an unexpected condition that prevented it from fulfilling the request.
- This could be because there is a problem with the response. In our case, it happened because the result wasn't able to be converted to JSON. NumPy bool and float cannot be interpreted by JSON, so we first convert them to normal python bool and float.

**Response `200`**
- OK success status. This means that the request was received, understood, and is being processed.

### Predicting in production
Example saved in <a href="https://github.com/SohailaDiab/365-Days-of-AI/blob/main/Week-2/Day-3/predict.py">predict.py</a>
- For debug mode run in terminal python `predict.py` (we set "debug=True")
- This is **only for developing**, for production we need to use something else, but not plain Flask, e.g. **gunicorn** or **waitress**

- To use Flask app for production, write in terminal:<br>
`gunicorn --bind 0.0.0.0:20303 predict:app`
- Preparing for production: gunicorn
- Running it on Windows with waitress _(gunicorn is not supprted by windows)_:<br>
`waitress-serve --listen=0.0.0.0:9696 predict:app`
