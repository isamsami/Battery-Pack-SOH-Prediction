# Battery Pack SOH Prediction

Overview
--------
This project combines a simple linear regression model for predicting battery State of Health (SOH) with a Streamlit-based chatbot interface. The chatbot uses a local battery dataset for prediction queries and routes general questions to Gemini.

Features
--------
- SOH prediction: Custom linear regression model trained on battery datasets.
- Interactive chatbot: Streamlit interface that routes SOH queries to the local model and general queries to Gemini.
- Excel uploads: Upload and edit a `.xlsx` file containing battery SOH records.
- Routing: Model handles SOH-specific queries; Gemini handles general questions.
- Visualization: Optional row demo and trend chart showing SOH over time.

Project structure
-----------------
- `venv/` — virtual environment (not checked in)
- `.env` — stores API key (keep secret)
- `.gitignore` — excludes sensitive files such as `.env`
- `PulseBat Dataset.xlsx` — dataset used for training/evaluation
- `README.md` — this file
- `requirements.txt` — list of required dependencies
- `script.py` — main Streamlit chatbot application
- `SOHpredicter.ipynb` — notebook used to build the linear regression model
- `soh_battery_model.pkl` — serialized model used by `script.py`

Installation & usage
--------------------
1. Clone the repository:
   ```bash
   git clone https://github.com/isamsami/Battery-Pack-SOH-Prediction.git
   cd Battery-Pack-SOH-Prediction
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # macOS / Linux
   source venv/bin/activate
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up API key:
   - Obtain a Gemini API key from Gemini AI Studio.
   - Add the key to a `.env` file (or `secrets.toml` for Streamlit Cloud). Example `.env`:
     ```
     GEMINI_API_KEY="your_api_key_here"
     ```

5. Run the application:
   ```bash
   streamlit run script.py
   ```

Requirements
------------
(Also listed in `requirements.txt`)  
- Python 3.9+ (if you encounter issues on newer versions, try 3.11)
- streamlit
- pandas
- numpy
- scikit-learn
- python-dotenv
- google-generativeai (Gemini client)
- pickle (stdlib)

Training information & notes
----------------------------
- Features used: U1–U20 voltages (note: this project used U1–U20 instead of the original U1–U21).
- Target: `SOH` column.
- Model: Linear Regression; saved as `soh_battery_model.pkl` for deployment.
- Noise injection: previously commented out for robustness testing. For production, train on clean, representative data.

Troubleshooting
---------------
- SOH outputs unexpectedly large (e.g., 3.5 instead of ~0.9): ensure the target is set correctly:
  ```python
  y = dataset["SOH"]
  ```
  not `ave_SOH`.
- Gemini API errors: verify the API key in `.env` or `secrets.toml`.
- Excel file not found: confirm `PulseBat Dataset.xlsx` is in the project root.
- Streamlit crashes: verify your Python environment and pinned dependency versions in `requirements.txt`.

License
-------
This project is provided for educational and demonstration purposes only. It is not licensed for commercial use, redistribution, or production deployment. Feel free to study, modify, and run the code locally.

Notes & next steps
------------------
- Adding a `LICENSE` file to change reuse terms.
- Pin dependency versions in `requirements.txt` for reproducible installs.
- Add examples/screenshots and a sample `.env.example` showing expected variables.
