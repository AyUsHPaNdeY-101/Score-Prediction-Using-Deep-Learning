from flask import Flask, request, render_template
import joblib
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

model = load_model("model/ipl_model.keras")
scaler = joblib.load("model/scaler.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    runs = float(request.form['runs'])
    wickets = float(request.form['wickets'])
    overs = float(request.form['overs'])
    runs_last_5 = float(request.form['runs_last_5'])
    wickets_last_5 = float(request.form['wickets_last_5'])

    input_data = np.array([[runs, wickets, overs, runs_last_5, wickets_last_5]])
    
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    return render_template('index.html', prediction_text=f'Predicted Final Score: {int(prediction[0][0])}')

if __name__ == "__main__":
    app.run(debug=True)