import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('student_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Student Math Score Prediction App")
st.write("Predict a student's math score based on input features.")

# --- Input fields ---
# Gender
gender = st.selectbox("Gender", ["female", "male"])
gender_male = 1 if gender == "male" else 0

# Parental Level of Education
parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)

# Map parental education to numeric values
education_mapping = {
    "some high school": 0,
    "high school": 1,
    "some college": 2,
    "associate's degree": 3,
    "bachelor's degree": 4,
    "master's degree": 5
}
parental_level_of_education_encoded = education_mapping[parental_level_of_education]

# Test Preparation Course
test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)
test_preparation_course_none = 1 if test_preparation_course == "none" else 0

# Scores
reading_score = st.slider("Reading Score", 0, 100, 50)
writing_score = st.slider("Writing Score", 0, 100, 50)

# --- Prepare input DataFrame ---
input_data = pd.DataFrame({
    "parental level of education": [parental_level_of_education_encoded],
    "test preparation course_none": [test_preparation_course_none],
    "reading score": [reading_score],
    "writing score": [writing_score],
    "gender_male": [gender_male]
})

# --- Prediction ---
if st.button("Predict Math Score"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Math Score: {prediction[0]:.2f}")
