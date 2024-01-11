import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model and vectorizer
model = pickle.load(open('Recruit_VADS_model.pkl', 'rb'))
vectorizer = pickle.load(open('Tfidf_Vectorizer.pkl', 'rb'))

# Load your resume data
candidates = pd.read_csv('Modifiedresumedata_data.csv')

# Define a function to get relevancy score for each candidate
def get_relevancy_score(job_title, skills, certification, experience):
    # Combine the job details into a single string
    combined_features = f"{job_title} {experience} {certification} {skills}"
    
    # Vectorize the combined features
    input_vector = vectorizer.transform([combined_features])
    
    # Predict the relevancy scores using the trained model
    relevancy_scores = model.predict(input_vector)

    # Combine the relevancy scores with the candidates data
    candidates['Relevancy Score'] = relevancy_scores
    
    # Sort the candidates by the relevancy score in descending order
    sorted_candidates = candidates.sort_values(by='Relevancy Score', ascending=False)
    
    return sorted_candidates.head(5)


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
        sorted_resumes = get_relevancy_score(form_data['role'], form_data['skills'],'0',form_data['experience'])

        # Display top 5 relevant candidates
        st.write("Top 5 Relevant Candidates:")
        st.dataframe(sorted_resumes)
    else:
        st.write("Please input job details and click 'Apply' to show relevant candidates.")

st.caption("Output with relevancy score will be shown.")
