Overview
This project integrates a linear regression model to predict the state of health (SOH) of batteries with a chatbot interface using streamlit. The chatbot features a dataset of batteries which is used to refer to in order to provide accurate results. The chatbot also is able to answer general questions whether it be able batteries or other inquiries via Gemini AI.
Features
SOH prediction: Using our custom linear regression model trained on battery datasets 
Interactive Chatbot: Built with Streamlit, combining our own machine learning model for predictions and Gemini api to ask gemini general questions
Excel uploads: The battery SOH has been documented in a .xlsx file for use already and can be be edited to add or delete battery SOH from that dataset
Routing: SOH queries go to the linear regression model and general queries go to Gemini
Visualization: Optional row demo and trend chart showing SOH trends are available
Project Structure
Venv (virtual environment)
.env (stores API key)
.gitignore (keeps API key hidden) 
PulseBat Dataset.xlsx (dataset we used)
README.md (this file)
requirements.txt (list of required dependencies to install)
script.py (main program where we run and execute the chatbot)
SOHpredicter.ipynb (linear regression model)
soh_battery_model.pkl (the model in .pkl file for use in script)

Installation & Usage
Clone the Github repo
git clone https://github.com/yourusername/battery-soh-chatbot.git
cd battery-soh-chatbot


Install all dependencies in requirements.txt
pip install -r requirements.txt
 Set up API key
Get API key from Gemini AI studio and past it in .env file
Run the application
streamlit run script.py
 
Requirements
These requirements are also listed in requirements.txt
Python 3.9+ (if using 3.14 may have to downgrade to 3.11 if giving you issues)
Streamlit
Pandas
NumPy
scikit‑learn
python‑dotenv
Google‑generativeai
pickle

Training Information & Notes
Features: U1–U20 voltages(instead of the original U1-U21 values).
Target: SOH column.
Model: Linear Regression.
Saved as soh_battery_model.pkl for deployment.
Noise injection was commented out but can be used for robustness testing, but production model should be trained on clean data.

Troubleshooting
SOH outputs were 3.5 instead of 0.9 → Ensured target y = dataset["SOH"], not ave_SOH.
Gemini API errors → Check .env or secrets.toml for correct API key.
Excel file not found → Confirm PulseBat Dataset.xlsx is in the project root.
Streamlit crashes → Verify Python environment and pinned dependencies in requirements.txt.
Liscence
This project is provided for educational and demonstration purposes only. It is not licensed for commercial use, redistribution, or production deployment. Feel free to study, modify, and run the code locally for learning and experimentation.