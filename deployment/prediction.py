import pickle
import pandas as pd
import streamlit


# Load the model is XGB
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_default(features):

    # Predict using the model
    prediction = model.predict(features)
    return prediction[0]