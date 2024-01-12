import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the model and vectorizer
def load_artifacts():
    with open('Recruit_VADS_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('Tfidf_Vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return model, vectorizer

# Load candidate data
def load_candidate_data():
    return pd.read_csv('Modifiedresumedata_data.csv')

# Predict relevancy scores
def predict_relevancy(model, vectorizer, input_data):
    relevancy_scores = []

    for _, candidate_row in candidate_data.iterrows():
        # Combine user input and candidate data into a single string
        combined_input = ' '.join([input_data['Role'], str(input_data['Experience']),
                                   input_data['Certifications'], input_data['Skills']])
        X = vectorizer.transform([combined_input])

        # Use the model to predict relevancy score
        score = model.predict(X)
        relevancy_scores.append(score[0])

    candidate_data['RelevancyScore'] = relevancy_scores
    top_candidates = candidate_data.nlargest(5, 'RelevancyScore')
    return top_candidates[['Candidate Name', 'Email ID', 'RelevancyScore']]

# Streamlit UI layout
st.set_page_config(page_title="Recruit VADS", layout="wide")

header_image_path = "Header.png"  # Adjust the path as necessary
st.image(header_image_path, width=700)

col1, col2 = st.columns([1, 2])

# Initialize or reset session state
if 'form_data' not in st.session_state:
    st.session_state['form_data'] = {'Role': '', 'Experience': '', 'Certifications': '', 'Skills': ''}
    st.session_state['submitted'] = False

def clear_form():
    st.session_state['form_data'] = {'Role': '', 'Experience': '', 'Certifications': '', 'Skills': ''}
    st.session_state['submitted'] = False

# Input fields for job details
with col1:
    with st.container():
        form_data = st.session_state['form_data']
        form_data['Role'] = st.text_input("Role", value=form_data['Role'])
        form_data['Experience'] = st.text_input("Experience", value=form_data['Experience'])
        form_data['Certifications'] = st.text_input("Certifications", value=form_data['Certifications'])
        form_data['Skills'] = st.text_input("Skills", value=form_data['Skills'])

        apply, clear = st.columns(2)
        if apply.button("Apply"):
            st.session_state['submitted'] = True
        if clear.button("Clear"):
            clear_form()

# Load model and vectorizer, and candidate data
model, vectorizer = load_artifacts()
candidate_data = load_candidate_data()

# Display results
with col2:
    if st.session_state['submitted']:
        top_candidates = predict_relevancy(model, vectorizer, form_data)
        st.write('Top Candidate Matches:')
        st.dataframe(top_candidates)
    else:
        st.write("Please input job details and click 'Apply' to show relevant candidates.")

st.caption("Output with relevancy score will be shown.")
