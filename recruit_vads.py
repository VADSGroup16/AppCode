import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

model = pickle.load(open('Recruit_VADS_model.pkl', 'rb'))
vectorizer = pickle.load(open('Tfidf_Vectorizer.pkl', 'rb'))

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
        # Process input data
        job_details = f"{form_data['role']} {form_data['experience']} {form_data['skills']}"
        job_details_vectorized = vectorizer.transform([job_details])

        # Make prediction
        relevancy_scores = model.predict(job_details_vectorized)

        # Assuming resume_data is preloaded with candidate names and contact details
        resume_data =pd.read_csv('Modifiedresumedata_data.csv')  # Replace with your actual dataframe
        resume_data['relevancy_score'] = relevancy_scores['Relevancy Score']

        # Sort the dataframe based on relevancy score
        sorted_resumes = resume_data.sort_values(by='relevancy_score', ascending=False)

        # Display results: Show sorted resumes with relevancy scores
        st.write("Relevant candidates:")
        st.dataframe(sorted_resumes)
    else:
        st.write("Please input job details and click 'Apply' to show relevant candidates.")

st.caption("Output with relevancy score will be shown.")
