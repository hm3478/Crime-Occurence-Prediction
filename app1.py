import json
import plotly
import pandas as pd
import numpy as np

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request
from plotly.graph_objs import Bar
import joblib
from sqlalchemy import create_engine


# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import datetime




model=pickle.load(open('model.pkl','rb'))
    







app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens



app = Flask(__name__)

@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')
@app.route('/login')
def login():
    return render_template('login.html')
def home():
	return render_template('home.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df) 

@app.route('/prediction1')
def prediction1():
    return render_template('index.html') 

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[x for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)[0]
    

    if prediction==1:
        return render_template('index.html',pred='This area is most vulnerable to larceny.'.format(prediction))
    elif prediction==2:
        return render_template('index.html',pred='This area is most vulnerable to public disorder.'.format(prediction))
    elif prediction==3:
        return render_template('index.html',pred='This area is most vulnerable to theft from motor vehicle.'.format(prediction))
    elif prediction==4:
        return render_template('index.html',pred='This area is most vulnerable to auto theft.'.format(prediction))
    elif prediction==5:
        return render_template('index.html',pred='This area is most vulnerable to drug alcohol.'.format(prediction))
    elif prediction==6:
        return render_template('index.html',pred='This area is most vulnerable to burglary.'.format(prediction))
    elif prediction==7:
        return render_template('index.html',pred='This area is vulnerable to all other crimes against people.'.format(prediction))
    elif prediction==8:
        return render_template('index.html',pred='This area is most vulnerable to aggravated assault.'.format(prediction))
    elif prediction==9:
        return render_template('index.html',pred='This area is most vulnerable to white collar crime.'.format(prediction))
    elif prediction==10:
        return render_template('index.html',pred='This area is most vulnerable to sexual assault.'.format(prediction))
    elif prediction==11:
        return render_template('index.html',pred='This area is most vulnerable to robbery.'.format(prediction))
    elif prediction==12:
        return render_template('index.html',pred='This area is most vulnerable to arson.'.format(prediction))
    elif prediction==13:
        return render_template('index.html',pred='This area is most vulnerable to murder.'.format(prediction))
    elif prediction==14:
        return render_template('index.html',pred='This area is most vulnerable to traffic accident.'.format(prediction))
    elif prediction==15:
        return render_template('index.html',pred='This area is vulnerable to other small crimes.'.format(prediction))


 
@app.route('/chart')
def chart():
    return render_template('chart.html')
@app.route('/prediction')
def prediction():
 	return render_template("home.html")
@app.route('/crime')
def crime():
 	return render_template("crime.html")
@app.route('/crimes')
def crimes():
 	return render_template("crimes.html")
@app.route('/total')
def total():
 	return render_template("total.html")
@app.route('/theft')
def theft():
    return render_template('theft.html')




if __name__ == '__main__':
         app.run(debug=True)
