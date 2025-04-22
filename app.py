# Run this for Flask app
#  Run Your App - python app.py

'''from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('salary_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    experience = float(request.form['experience'])
    prediction = model.predict(np.array([[experience]]))
    return render_template('index.html', prediction_text=f'Predicted Salary: ${prediction[0]:,.2f}')

if __name__ == '__main__':
    app.run(debug=True)'''


# Run this for Streamlit app
#  Run Your App -  streamlit run app.py

import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('salary_model.pkl')

# Streamlit App
st.title("💼 Salary Predictor")
st.write("Predict a salary based on years of experience using a trained Linear Regression model.")

# Input field
experience = st.number_input("Enter Years of Experience:", min_value=0.0, step=0.1, format="%.1f")

# Predict button
if st.button("Predict Salary"):
    prediction = model.predict(np.array([[experience]]))
    st.success(f"Predicted Salary: ${prediction[0]:,.2f}")
