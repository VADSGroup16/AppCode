import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Function to load model and vectorizer
def load_artifacts():
    with open('Recruit_VADS_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('Tfidf_Vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

# Load candidate data
def load_candidate_data():
    candidate_data_path = 'Modifiedresumedata_data.csv'
    candidate_data = pd.read_csv(candidate_data_path)
    return candidate_data

# Function to predict relevancy scores
def predict_relevancy(model, vectorizer, input_data, candidate_data):
    combined_input = ' '.join(input_data)
    X_input = vectorizer.transform([combined_input])
    candidate_features = candidate_data['Skills'] + ' ' + \
                         candidate_data['Role'] + ' ' + \
                         candidate_data['Certification']
    X_candidates = vectorizer.transform(candidate_features)
    candidate_scores = model.predict(X_candidates)
    candidate_data['RelevancyScore'] = candidate_scores
    sorted_candidates = candidate_data.sort_values(by='RelevancyScore', ascending=False)
    top_candidates = sorted_candidates.head(5)
    return top_candidates

# Streamlit app
st.title('Recruit VADS')

# Load model and vectorizer
model, vectorizer = load_artifacts()

# Load candidate data
candidate_data = load_candidate_data()

# Input fields for job details
role = st.text_input('Role')
experience = st.slider('Experience', 0, 50, 5)
certifications = st.text_area('Certifications', height=100)
skills = st.text_area('Skills', height=100)

# Button to apply
if st.button('Find Candidates'):
    input_data = [role, str(experience), certifications, skills]
    top_candidates = predict_relevancy(model, vectorizer, input_data, candidate_data)
    st.write(top_candidates)

# Run this in a terminal: streamlit run app.py
