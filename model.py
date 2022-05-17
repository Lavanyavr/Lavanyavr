import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

from sklearn.ensemble import RandomForestRegressor

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/predict', methods=['post'])

def predict():
    if request.method =='post':

        fixedAcidity = request.form["fixedAcidity"]
        volatileAcidity = request.form["volatileAcidity"]
        citricAcid = request.form['citricAcid']
        residualSugar = request.form['residualSugar']
        chlorides = request.form["chlorides"]
        freeSulfurDioxide = request.form["freeSulfurDioxide"]
        totalSulfurDioxide = request.form["totalSulfurDioxide"]
        density = request.form["density"]
        pH = request.form["pH"]
        sulphates = request.form["sulphates"]
        alcohol = request.form["alcohol"]

        data = [[float(fixedAcidity),float(volatileAcidity),float(citricAcid),float(residualSugar),float(chlorides),float(freeSulfurDioxide),
        float(totalSulfurDioxide),float(density),float(pH),float(sulphates),float(alcohol)]]
        rfr = pickle.load(open('winequality-red.pkl','rd'))
        prediction = rfr.predict(data)[0]

        return render_template('index.html', prediction=prediction)
if __name__=='__main__':
    app.run('')