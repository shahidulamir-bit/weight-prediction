import streamlit as st
import pandas as pd
import pickle
import numpy as np
from pathlib import Path



st.title("S.M Shahidul Amir's Streamlit App")
st.write("welcome to my website")

with open(r"D:\download\linear model\model.pkl", "rb") as file:
    model = pickle.load(file)

height = st.number_input("Enter your height (in meters):")
if st.button("Predict Weight"):
    if height > 0:
        height_value = float(height)
        prediction = model.predict(np.array([[height_value]]))
        weight = float(np.squeeze(prediction[0]))
        st.success(f"Predicted weight: {weight:.2f} kg")
    else:
        st.error("Please enter a valid height greater than 0.") 
                         

         


    





