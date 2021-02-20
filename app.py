#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import lime
import lime.lime_text

#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.sav', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/style.css')
def send_css():
  return app.send_static_file('style.css')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    int_features = []
    int_features.append(request.form.get('yes_cough'))
    int_features.append(request.form.get('yes_fever'))
    int_features.append(request.form.get('yes_sore_throat'))
    int_features.append(request.form.get('yes_shortness_of_breath'))
    int_features.append(request.form.get('yes_head_ache'))
    int_features.append(request.form.get('yes_age_60_and_above'))
    if request.form.get('male_gender') == "on":
        int_features.append(2)
    elif request.form.get('female_gender') == "on":
        int_features.append(1)
    elif request.form.get('other_gender') == "on":
        int_features.append(0)
    if request.form.get('yes_contact') == "on":
        int_features.append(2)    
    elif request.form.get('no_contact') == "on":
        int_features.append(1)
    elif request.form.get('other_contact') == "on":
        int_features.append(0)

    for i in range(len(int_features)):
        if int_features[i] == "on":
            int_features[i] = 1
        elif int_features[i] == None:
            int_features[i] = 0
        elif int_features[i] == "off":
            int_features[i] = 0
    
    print(int_features)

    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    covid_status = ''
    prob = 0
    print(prediction)
    if prediction == 0:
        covid_status = 'You are not displaying COVID-19 symptoms'
    elif prediction == 1:
        covid_status = 'You are likely displaying COVID-19 symptoms'

    return render_template('index.html', prediction_text=covid_status)

if __name__ == "__main__":
    app.run(debug=True)