import google.generativeai as genai #gemini sdk instead of openai
import pickle
import numpy as np
import streamlit as st
import pandas as pd

# chatbot can access excel file directly
df = pd.read_excel(r"C:\Users\user\OneDrive\Documents\GitHub\Battery-Pack-SOH-Prediction\content\PulseBat Dataset.xlsx")

# liear regression model for battery state of health prediction
with open("soh_battery_model.pkl", "rb") as file:
    model = pickle.load(file)

# gemini api configuration
genai.configure(api_key="AIzaSyCfb2_he_NtExQeMQWIeIRQPbQ6Dhjpfsg")
gemini_model = genai.GenerativeModel("gemini-pro")

# function to help predict state of health
def predict_soh(cell_data):
    X = np.array(cell_data).reshape(1, -1)
    soh_pred = model.predict(X)[0]
    return soh_pred

# streamlit ui
st.title("Battery Pack State of Health Chatbot")
user_input = st.text_input("What do you want:")

# handle user input
if user_input:
    # Simple keyword detection for SOH-related queries
    soh_keywords = ["soh", "battery health", "state of health", "check battery"]
    if any(keyword in user_input.lower() for keyword in soh_keywords):
        # Example values for U1–U21
        cell_data = [0.85, 0.9, 0.88, 0.87, 0.86, 0.84, 0.83, 0.82, 0.81,
                     0.8, 0.79, 0.78, 0.77, 0.76, 0.75, 0.74, 0.73, 0.72,
                     0.71, 0.7, 0.69]
        soh_pred = predict_soh(cell_data)

        threshold = 0.6
        status = "The battery is healthy." if soh_pred >= threshold else "The battery has a problem."

        st.write(f"Predicted SOH: {soh_pred:.2f}")
        st.write(status)
    else:
        # Use Gemini model for general queries
        response = gemini_model.generate_content(user_input)
        st.write(response.text)
