import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('student_model.pkl', 'rb') as f:
	model = pickle.load(f)

st.title('Student Mark Prediction App')
st.write('Predict student marks based on input features.')

# Example input fields (adjust according to your model's features)
gender = st.selectbox('Gender', ['female', 'male'])
parental_level_of_education = st.selectbox(
	'Parental Level of Education',
	[
		"some high school", "high school", "some college",
		"associate's degree", "bachelor's degree", "master's degree"
	]
)
test_preparation_course = st.selectbox('Test Preparation Course', ['none', 'completed'])
math_score = st.slider('Math Score', 0, 100, 50)
reading_score = st.slider('Reading Score', 0, 100, 50)

# Prepare input for prediction
input_data = pd.DataFrame({
	'parental level of education': [parental_level_of_education],
    'test preparation course': [test_preparation_course],
	'reading score': [reading_score]
    'math score': [math_score],
	'gender': [gender]
})

# If your model requires encoding, make sure to preprocess input_data accordingly

if st.button('Predict Marks'):
	prediction = model.predict(input_data)
	st.success(f'Predicted Marks: {prediction[0]:.2f}')

