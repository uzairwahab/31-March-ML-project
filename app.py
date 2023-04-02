from flask import Flask,request,jsonify,render_template
import pickle 
import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

##import redge regressor model and standred scaler pickle
ridge_model = pickle.load(open('Models/ridge.pk1', 'rb'))
stander_model = pickle.load(open('Models/scaler.pk1', 'rb'))

##Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pridictdata', methods = ['GET','POST'])
def pridict_datapoint():
    if request.method=='POST':
        Tempereature = float(request.form.get('Temp'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Temp'))
        Rain = float(request.form.get('Temp'))
        FFMC = float(request.form.get('Temp'))
        DMC = float(request.form.get('Temp'))
        ISI = float(request.form.get('Temp'))                             
        Classes = float(request.form.get('Temp'))
        Regon = float(request.form.get('Temp'))

        new_data_scaled = standard_scaler.transform([[Temp ,RH,Ws, Rain,FFMC,DMC,ISI,Classes,Region]]) 
        result= ridge_model.predict(new_data_scaled) 


        return render_template('home.html' ,result =result)  
    else:
        return render_template('home.html')




if __name__=="__main__":
    app.run(host="0.0.0.0")
