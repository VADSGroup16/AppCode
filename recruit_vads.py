import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the model and vectorizer
# Load candidate data
@st.cache(allow_output_mutation=True)
def load_candidate_data():
    return pd.read_csv('Modifiedresumedata_data.csv')

# Predict relevancy scores
def predict_relevancy(vectorizer, input_data, candidate_data):
    # Make a copy of the candidate data to avoid mutation
    candidate_data = candidate_data.copy()

    combined_input = ' '.join([input_data['Role'], str(input_data['Experience']), 
                               input_data['Certifications'], input_data['Skills']])
    X_input = vectorizer.transform([combined_input])

    # Calculate relevancy scores based on cosine similarity
    candidate_scores = []
    for _, row in candidate_data.iterrows():
        candidate_combined = ' '.join([row['Role'], str(row['Experience']), 
                                       row['Certification'], row['Skills']])
        X_candidate = vectorizer.transform([candidate_combined])
        score = cosine_similarity(X_input, X_candidate)
        candidate_scores.append(score[0][0])

    candidate_data['RelevancyScore'] = candidate_scores
    # Convert scores to percentages and round to two decimal places
    candidate_data['RelevancyScore'] = (candidate_data['RelevancyScore'] * 100).round(2)
    
    top_candidates = candidate_data.nlargest(5, 'RelevancyScore')
    return top_candidates[['Candidate Name', 'Email ID', 'RelevancyScore']]

# Streamlit app
st.title('Recruit VADS Candidate Finder')

# Load model and vectorizer
model, vectorizer = load_artifacts()

# Load candidate data
candidate_data = load_candidate_data()

# Input fields for job details
user_input = {
    'Role': st.text_input('Role'),
    'Experience': st.text_input('Experience'),
    'Certifications': st.text_area('Certifications'),
    'Skills': st.text_area('Skills')
}

# Button to find candidates
if st.button('Find Candidates'):
    top_candidates = predict_relevancy(vectorizer, user_input, candidate_data)
    st.write('Top Candidate Matches:')
    st.dataframe(top_candidates)

# Run this in a terminal: streamlit run your_script.py
