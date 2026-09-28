
import os
import joblib
import streamlit as st
import joblib
from pathlib import Path

model = joblib.load(
    Path(__file__).parent / "Pipeline_placement_model.pkl"
)

model_path = os.path.join(os.path.dirname(__file__), "Pipeline_placement_model.pkl")
model = joblib.load(model_path)


st.title("🎓 College Placement Predictor")

st.write("Enter the student's details:")

iq = st.number_input("IQ", min_value=0, max_value=200, value=100)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=7.0)
communication = st.number_input(
    "Communication Skills", min_value=0, max_value=10, value=5
)
projects = st.number_input(
    "Projects Completed", min_value=0, max_value=20, value=2
)
internship = st.selectbox(
    "Internship Experience", [0, 1]
)

if st.button("Predict Placement"):

    student = [[iq, cgpa, communication, projects, internship]]

    prediction = model.predict(student)[0]
    probability = model.predict_proba(student)[0][1]

    if prediction == 1:
        st.success(f"Placed ✅ — Probability: {probability:.2%}")
    else:
        st.error(f"Not Placed ❌ — Probability: {probability:.2%}")