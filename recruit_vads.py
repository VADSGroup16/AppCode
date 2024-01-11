import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model and vectorizer
model = pickle.load(open('Recruit_VADS_model.pkl', 'rb'))
vectorizer = pickle.load(open('Tfidf_Vectorizer.pkl', 'rb'))

# Load your resume data
resume_data = pd.read_csv('Modifiedresumedata_data.csv')

# Define a function to get relevancy score for each candidate
def get_relevancy_scores(job_title, skills, experience):
    relevancy_scores = []
    for _, row in resume_data.iterrows():
        combined_features = f"{job_title} {skills} {experience} {row['Candidate Info']}"  # Adjust as per your data columns
        input_vector = vectorizer.transform([combined_features])
        score = model.predict(input_vector)
        relevancy_scores.append(score[0])  # Assuming model.predict returns a single score in an array
    
    return relevancy_scores

# Set page configuration
st.set_page_config(page_title="Recruit VADS", layout="wide")

header_image_path = "Header.png"  # Adjust the path as necessary
st.image(header_image_path, width=700)

col1, col2 = st.columns([1, 2])

# Initialize or reset session state
if 'form_data' not in st.session_state:
    st.session_state['form_data'] = {'role': '', 'experience': '', 'skills': ''}
    st.session_state['submitted'] = False
    st.session_state['clear_requested'] = False

def clear_form():
    st.session_state['form_data'] = {'role': '', 'experience': '', 'skills': ''}
    st.session_state['submitted'] = False
    st.session_state['clear_requested'] = False

with col1:
    with st.container():
        form_data = st.session_state['form_data']
        form_data['role'] = st.text_input("Role", value=form_data['role'])
        form_data['experience'] = st.text_input("Experience", value=form_data['experience'])
        form_data['skills'] = st.text_input("Skills", value=form_data['skills'])

        apply, clear = st.columns(2)
        with apply:
            if st.button("Apply"):
                st.session_state['submitted'] = True
        with clear:
            if st.button("Clear"):
                clear_form()

with col2:
    if st.session_state['submitted']:
        # Get relevancy scores for each candidate
        scores = get_relevancy_scores(form_data['role'], form_data['skills'], form_data['experience'])
        resume_data['Relevancy Score'] = scores
        sorted_resumes = resume_data.sort_values(by='Relevancy Score', ascending=False).head(5)

        # Display top 5 relevant candidates
        st.write("Top 5 Relevant Candidates:")
        st.dataframe(sorted_resumes)
    else:
        st.write("Please input job details and click 'Apply' to show relevant candidates.")

st.caption("Output with relevancy score will be shown.")
