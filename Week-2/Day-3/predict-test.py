#!/usr/bin/env python
# coding: utf-8

import requests 

url = 'http://192.168.1.104:20303/predict'

customer_id = 'xyz-123'
customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
}

# We now want to send this customer in a POST request
response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('Sending promo email to %s' % customer_id)
else:
    print('Will not send promo email to %s' % customer_id)
