""" 
Intro to Flask:
- Writing a simple ping/pong app
- Querying it with `curl` and browser:
    curl http://192.168.1.104:20303/ping
"""
from flask import Flask

# Create flask app
app = Flask('ping')

# Put a decorator (a way to add extra functionality to the function)
# In route we will specify which address this function will live
@app.route('/ping', methods=['GET'])
def ping():
    return "PONG"

# Run app in debug mode
# This should live inside the main script
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=20303)