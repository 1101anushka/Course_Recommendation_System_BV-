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
modelRE = pickle.load(open('models/modelRE.pkl', 'rb'))
modelDE = pickle.load(open('models/modelDE.pkl', 'rb'))

@app.route('/')
def code1():
    return render_template('code1.html')
@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/faq')
def faq():
    return render_template('faq.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['POST','GET'])
def submit():
    
        # getting input with name = fname in HTML form
        rt= request.form.get("rate")
        review = request.form.get("desc")
        
        if request.method == "POST":

        # write to file
            with open('C:/Users/asus/Desktop/BTCS_G31/EXECUTABLE PROJECT/models/fb.txt', 'a') as f:
                #f.write("%s %s \n" % str((review), str(rate)))
                f.write('{0} {1} \n'.format(review, rt))

        return render_template('code1.html')

@app.route('/predict', methods=['POST','GET'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    predictionRE = modelRE.predict(final_features)
    predictionDE = modelDE.predict(final_features)
    result1 = predictionRE[0][0]
    result2 = predictionRE[0][1]
    result3 = predictionDE[0][0]
    result4 = predictionDE[0][1]
    if(result1==0):
        s1='Blockchain'
    elif(result1==1):
        s1='Electronic Commerce'
    elif(result1==2):
        s1='Enterprise Resource Planning'
    elif(result1==3):
        s1='IT in Business'
    elif(result1==4):
        s1='Organisational Behavior'
    elif(result1==5):
        s1='Parallel Computing'
    elif(result1==6):
        s1='Software as a Service'
    if(result2==0):
        s2='Blockchain'
    elif(result2==1):
        s2='Electronic Commerce'
    elif(result2==2):
        s2='Enterprise Resource Planning'
    elif(result2==3):
        s2='IT in Business'
    elif(result2==4):
        s2='Organisational Behavior'
    elif(result2==5):
        s2='Parallel Computing'
    elif(result2==6):
        s2='Software as a Service'
    elif(result2==7):
        s2='Client-Server Computing and Applications'
    if(result3==0):
        s3='Computer Vision'
    elif(result3==1):
        s3='Distributed Computing'
    elif(result3==2):
        s3='Digital Image Processing'
    elif(result3==3):
        s3='Data Mining and Warehousing'
    elif(result3==4):
        s3='Internet of Things'
    elif(result3==5):
        s3='Pattern Recognition'
    elif(result3==6):
        s3='Robotics and Automation'
    elif(result3==7):
        s3='Real Time Systems'
    elif(result3==8):
        s3='Soft Computing'
    if(result4==0):
        s4='Computer Vision'
    elif(result4==1):
        s4='Distributed Computing'
    elif(result4==2):
        s4='Digital Image Processing'
    elif(result4==3):
        s4='Data Mining and Warehousing'
    elif(result4==4):
        s4='Internet of Things'
    elif(result4==5):
        s4='Pattern Recognition'
    elif(result4==6):
        s4='Robotics and Automation'
    elif(result4==7):
        s4='Real Time Systems'
    elif(result4==8):
        s4='Soft Computing'
    elif(result4==9):
        s4='Big Data Analytics'
    return render_template('electives.html',
                               predictionRE1=s1,predictionRE2=s2, predictionDE3=s3,predictionDE4=s4)
       
         
    #return render_template('electives.html', predictionRE=predictionRE, predictionDE=predictionDE,  
                              # )
if __name__ == "__main__":
    app.run(debug=True)
