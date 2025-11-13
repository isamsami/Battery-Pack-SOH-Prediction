import numpy as np
import pickle

# Load model once
with open("model/battery_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_battery_soh(cell_values, threshold=0.6):
    pack_soh = np.mean(cell_values)  # aggregation method
    predicted_soh = model.predict([[pack_soh]])[0]
    status = "The battery is healthy." if predicted_soh >= threshold else "The battery has a problem."
    return predicted_soh, status
