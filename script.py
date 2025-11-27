import google.generativeai as genai #gemini sdk instead of openai
import pickle
import numpy as np
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import re

# load environment variables
load_dotenv()

# chatbot can access excel file directly
df = pd.read_excel("PulseBat Dataset.xlsx")



# load linear regression model and rows used for battery state of health prediction
with open("soh_battery_model.pkl", "rb") as file:
    model = pickle.load(file)
feature_cols = [
    "U1","U2","U3","U4","U5","U6","U7","U8","U9","U10",
    "U11","U12","U13","U14","U15","U16","U17","U18","U19","U20"
]



# gemini api configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-2.5-flash")

# Predict SOH from rows
def predict_from_row(row_index):
    if row_index < 0 or row_index >= len(df):
        return None, "Row number out of range."

    row = df.iloc[row_index] 
    cell_data = row[feature_cols].values.reshape(1, -1) 
    soh_pred = model.predict(cell_data)[0]

    return soh_pred, None




# streamlit ui
st.title("Battery Pack State of Health Chatbot")
user_input = st.text_input("What do you want:")
threshold = st.slider(
    "SOH threshold",        # label
    min_value=0.0,          # lower bound
    max_value=1.0,          # upper bound
    value=0.6,              # default
    step=0.05               # increment
)

# handle user input
if user_input:
    # Simple keyword detection for SOH-related queries
    soh_keywords = ["soh", "battery health", "state of health", "check battery"]
    if any(keyword in user_input.lower() for keyword in soh_keywords):

        # Look for a row number in the query
        match = re.search(r"row\s*(\d+)", user_input.lower())

        if match:
            row_num = int(match.group(1)) - 1  # Convert to 0-index

            soh_pred, error = predict_from_row(row_num)

            if error:
                st.error(error)
            else:
                status = "Healthy" if soh_pred >= threshold else "Potential Issue"

                st.write(f"Predicted SOH: {soh_pred:.3f}")
                st.write(f"Status: {status}")

        else:
            st.info("Please format your question like this for better performance: Predict SOH for row 1")
   
    else:
        # Use Gemini model for general queries
        response = gemini_model.generate_content(user_input)
        st.write(response.text)


#these print fucntions are for testing purposes

#print("Model type:", type(model))
#print("Intercept:", model.intercept_)
#print("Coefficients shape:", model.coef_.shape)
#print("Model expects:", model.n_features_in_)
#print("Feature columns:", feature_cols)

