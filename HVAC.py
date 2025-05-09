import pickle
import streamlit as st
import pandas as pd

df = pd.read_csv("sensor.csv", delimiter=";")

load = open('Random_model3.pkl', 'rb')
model = pickle.load(load)

def predict(*sensor_values):
    sensor_values = [float(x) for x in sensor_values]
    prediction = model.predict([sensor_values])
    return prediction

def main():
    st.title("🔧 Predictive Maintenance for HVAC Pumps")
    st.subheader("Enter Sensor Data to Predict Pump Condition")
    st.markdown("This tool uses sensor readings to predict if the HVAC pump is **BROKEN**, **NORMAL**, or in **RECOVERY** mode.")

    sensor_names = [f"sensor_{i:02}" for i in range(52) if i != 15]  # skip sensor_15
    cols = st.columns(4)
    sensor_values = {}

    for idx, sensor in enumerate(sensor_names):
        col = cols[idx % 4]
        sensor_values[sensor] = col.text_input(sensor.capitalize() + ":")

    if st.button("Predict"):
        if all(sensor_values[s] != "" for s in sensor_names):
            inputs = [sensor_values[s] for s in sensor_names]
            result = predict(*inputs)
            if result == 0:
                st.success("Prediction: 🚨 BROKEN")
            elif result == 1:
                st.success("Prediction: ✅ NORMAL")
            else:
                st.success("Prediction: 🔄 RECOVER")
        else:
            st.warning("Please fill in all sensor values.")

if __name__ == "__main__":
    main()
