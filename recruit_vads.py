import streamlit as st
import pandas as pd
import pickle

# Load model and vectorizer
model = pickle.load(open('Recruit_VADS_model.pkl', 'rb'))
vectorizer = pickle.load(open('Tfidf_Vectorizer.pkl', 'rb'))

# Load your resume data
# Example: resume_data = pd.read_csv('path_to_resume_data.csv')
# Ensure resume_data has columns like 'Candidate Name', 'Email ID', etc.

# Define a function to get relevancy score
def get_relevancy_score(job_title, skills, experience):
    # Combine the features into a single string
    combined_features = f"{job_title} {skills} {experience}"
    
    # Vectorize the input features
    input_vector = vectorizer.transform([combined_features])
    
    # Make prediction (assuming your model's predict method returns relevancy scores)
    relevancy_scores = model.predict(input_vector)

    # Create a DataFrame to display results
    output = pd.DataFrame()
    output['Relevancy Score'] = relevancy_scores
    # Add additional candidate info from resume_data here
    return output

# Streamlit UI code
# ...

with col2:
    if st.session_state['submitted']:
        # Get output from the function
        output = get_relevancy_score(form_data['role'], form_data['skills'], form_data['experience'])

        # Display results
        st.write("Relevant candidates:")
        st.dataframe(output)
    else:
        st.write("Please input job details and click 'Apply' to show relevant candidates.")
