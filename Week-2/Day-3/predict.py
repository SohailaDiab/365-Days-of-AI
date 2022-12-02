
import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
  dv, model = pickle.load(f_in)

# Create flask app
app = Flask('churn')
# We want to send info about the customer, so we use POST
@app.route('/predict', methods=['POST'])

def predict():
    # Take the body of the request, which is customer features,
    # assume that it is json and it'll parse it
    # and turn it into Python dictionary
    customer = request.get_json()

    # Turn this customer to feature matrix
    X = dv.transform([customer])
    # Probability of churning
    y_pred = model.predict_proba(X)[0, 1]
    # Churn will be true if probability is above 0.5
    churn = y_pred >= 0.5

    # Response will be returned as json from this dict
    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn) # Turn numPy bool into usual Py bool
                             # Since json cannot interpret numpy bool
                             # Same thing for float
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=20303)

# customer = {
#     "gender": "female",
#     "seniorcitizen": 0,
#     "partner": "yes",
#     "dependents": "no",
#     "phoneservice": "no",
#     "multiplelines": "no_phone_service",
#     "internetservice": "dsl",
#     "onlinesecurity": "no",
#     "onlinebackup": "yes",
#     "deviceprotection": "no",
#     "techsupport": "no",
#     "streamingtv": "no",
#     "streamingmovies": "no",
#     "contract": "month-to-month",
#     "paperlessbilling": "yes",
#     "paymentmethod": "electronic_check",
#     "tenure": 1,
#     "monthlycharges": 29.85,
#     "totalcharges": 29.85
# }