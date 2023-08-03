# Import the necessary libraries
import streamlit as st
import requests
import json
from PIL import Image

setosa = Image.open('setosa.jpg')
versi = Image.open('versi.jpg')
virgi = Image.open('virginica.jpg')
# Define the FastAPI server endpoint
FASTAPI_SERVER_ENDPOINT = 'https://alexgdockerbota.azurewebsites.net/predict'

# Create the Streamlit form
st.title("Predicition des especes d'Iris")
sepal_length = st.number_input('Longueur du sepal')
sepal_width = st.number_input('Largeur du sepal')
petal_length = st.number_input('Longueur du petal')
petal_width = st.number_input('Largeur du petal')

if st.button('Prediction'):
    payload = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }
    response = requests.post(FASTAPI_SERVER_ENDPOINT, json=payload)
    if response.status_code == 200:
        prediction = response.json()['prediction']
        probability = response.json()['probability']
        st.write(f'Espece : {prediction}')
        st.write(f'Precision de la prediction : {probability} %')
    else:
        st.write(f'Some error occurred: {response.text}')

    if prediction == "setosa":
        st.image(setosa)
    elif prediction == "virginica":
        st.image(virgi)
    elif prediction == "versicolor":
        st.image(versi)
