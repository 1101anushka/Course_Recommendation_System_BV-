# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
modelRE = pickle.load(open('modelRE.pkl', 'rb'))
modelDE = pickle.load(open('modelDE.pkl', 'rb'))
@app.route('/', methods=['POST','GET'])
def form():
    return render_template('form.html')

@app.route('/predictRE', methods=['POST','GET'])
def predictRE():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    predictionRE = modelRE.predict(final_features)
    output=modelRE.predict(final_features)
    return render_template('reading.html',
                               prediction_text='The best two recommended reading electives are $ {}'.format(output)
                               )

@app.route('/predictDE', methods=['POST','GET'])
def predictDE():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    predictionDE = modelDE.predict(final_features)
    output=modelDE.predict(final_features)
    return render_template('discipline.html',
                               prediction_text='The best two recommended discipline electives are $ {}'.format(output)
                               )

if __name__ == "__main__":
    app.run(debug=True)