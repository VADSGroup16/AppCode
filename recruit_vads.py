import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model and vectorizer
model = pickle.load(open('Recruit_VADS_model.pkl', 'rb'))
vectorizer = pickle.load(open('Tfidf_Vectorizer.pkl', 'rb'))

# Load your resume data
# Adjust the path and columns as per your actual data file
resume_data = pd.read_csv('Modifiedresumedata_data.csv')

# Define a function to get relevancy score
def get_relevancy_score(job_title, skills, experience):
    # Combine the features into a single string
    combined_features = f"{job_title} {skills} {experience}"
    
    # Vectorize the input features
    input_vector = vectorizer.transform([combined_features])
    
    # Make prediction (assuming your model's predict method returns relevancy scores)
    relevancy_scores = model.predict(input_vector)

    # Create a DataFrame to display results
    output = pd.DataFrame(resume_data, columns=['Candidate Name', 'Email ID'])
    output['Relevancy Score'] = relevancy_scores
    return output.sort_values(by='Relevancy Score', ascending=False)

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
        # Process input data and get output
        output = get_relevancy_score(form_data['role'], form_data['skills'], form_data['experience'])

        # Display results: Show sorted resumes with relevancy scores
        st.write("Relevant candidates:")
        st.dataframe(output)
    else:
        st.write("Please input job details and click 'Apply' to show relevant candidates.")

st.caption("Output with relevancy score will be shown.")
