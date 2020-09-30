from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["POST"])
def predict():
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: LIMIT_BAL
        in: query
        type: number
        required: true
      - name: PAY_1
        in: query
        type: number
        required: true
      - name: PAY_2
        in: query
        type: number
        required: true
      - name: PAY_3
        in: query
        type: number
        required: true
      - name: PAY_4
        in: query
        type: number
        required: true
      - name: PAY_5
        in: query
        type: number
        required: true
      - name: PAY_6
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    LIMIT_BAL=request.args.get("LIMIT_BAL")
    PAY_1=request.args.get("PAY_1")
    PAY_2=request.args.get("PAY_2")
    PAY_3=request.args.get("PAY_3")
    PAY_4=request.args.get("PAY_4")
    PAY_5=request.args.get("PAY_5")
    PAY_6=request.args.get("PAY_6")
    
    
    prediction=model.predict([[LIMIT_BAL, PAY_1, PAY_2, PAY_3, PAY_4,PAY_5, PAY_6]])
    print(prediction)
    if prediction>0.5:
        return "Fraud"+str(prediction)
    else:
        return "Not Fraud"+str(prediction)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    
    