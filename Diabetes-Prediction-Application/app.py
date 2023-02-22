import os
os.system('pip install requirements.txt')

from flask import Flask,render_template, request
import pickle
import numpy as np
import os



#loading the random forest classifier model
here = os.path.dirname(os.path.abspath(__file__))
filename=os.path.join(here,"diabetes-prediction-model.pkl")
cls=pickle.load(open(filename,'rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    if request.method=="POST":
        if request.method == 'POST':
            preg = int(request.form['pregnancies'])
            glucose = int(request.form['glucose'])
            bp = int(request.form['bloodpressure'])
            st = int(request.form['skinthickness'])
            insulin = int(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = int(request.form['age'])
            
            data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
            my_prediction = cls.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
