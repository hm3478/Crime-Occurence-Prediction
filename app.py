from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


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


if __name__ == '__main__':
    app.run(debug=True)