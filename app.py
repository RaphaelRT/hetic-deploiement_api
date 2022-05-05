
from flask import Flask, request
from flask import jsonify
from flask import request
from flask import abort
from json import loads
import numpy as np
from sklearn.linear_model import LinearRegression


with open('data/model.json', 'r') as f:
  content = f.read()
  model = loads(content)


predictor = LinearRegression(n_jobs=-1)
predictor.coef_ = np.array(model)
predictor.intercept_ = np.array([0])

app = Flask(__name__)

@app.route('/')
def hello_world():
  params = request.args.get('input')
  parameters = params.split(",")
  X_TEST = [list(map(int, parameters[0:3]))]
  outcome = predictor.predict(X=X_TEST)
  return str(outcome[0]) + "\n"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
  print("Server is running")