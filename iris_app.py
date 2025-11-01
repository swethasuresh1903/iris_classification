import pickle
import streamlit as st

# Load trained model
with open('iris_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load label encoder
with open('label_encoder.pkl', 'rb') as file:
    le = pickle.load(file)

st.title("Iris Flower Species Prediction 🌸")

# Streamlit sliders for input
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

if st.button("Predict Species"):
    sample = [[sepal_length, sepal_width, petal_length, petal_width]]
    pred_encoded = model.predict(sample)
    species = le.inverse_transform(pred_encoded)[0]
    st.success(f"The predicted Iris species is: {species}")
