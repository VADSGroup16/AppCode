import streamlit as st
import pandas as pd

# Function to simulate fetching candidate data
def fetch_candidates(role, experience, certifications, skills):
    # Dummy data for the example
    return pd.DataFrame({
        'Candidate Name': ['Alice Smith', 'Bob Jones', 'Carol Johnson'],
        'Contact Details': ['alice@example.com', 'bob@example.com', 'carol@example.com'],
        'Relevancy Score': [95, 90, 88]
    })

# Set page configuration
st.set_page_config(page_title="Recruit VADS", layout="wide")

# Display the header image in the middle of the page
header_image_path = "Header.png"  # Path to the header image file
st.image(header_image_path, use_column_width=True)

# Create a two-column layout for the form and candidates table
col1, col2 = st.columns([1, 2])

with col1:
    # Using container to keep the form compact
    with st.container():
        # Initialize session states for form fields
        if 'role' not in st.session_state:
            st.session_state['role'] = ''
        if 'experience' not in st.session_state:
            st.session_state['experience'] = ''
        if 'certifications' not in st.session_state:
            st.session_state['certifications'] = ''
        if 'skills' not in st.session_state:
            st.session_state['skills'] = ''

        # Define the form
        with st.form(key='job_details_form'):
            role = st.text_input("Role", value=st.session_state['role'])
            experience = st.text_input("Experience", value=st.session_state['experience'])
            certifications = st.text_input("Certifications", value=st.session_state['certifications'])
            skills = st.text_input("Skills", value=st.session_state['skills'])
            submitted = st.form_submit_button("Apply")
            cleared = st.form_submit_button("Clear")

            # Clear the form if the clear button is pressed
            if cleared:
                st.session_state['role'] = ''
                st.session_state['experience'] = ''
                st.session_state['certifications'] = ''
                st.session_state['skills'] = ''
                st.experimental_rerun()

# The right column will display the candidates
with col2:
    if submitted:
        # Simulate fetching data based on form input (this would be your actual data retrieval logic)
        candidates = fetch_candidates(role, experience, certifications, skills)
        # Create a dataframe and display it on the right column
        st.dataframe(candidates)
    else:
        # Instructions or placeholder content
        st.write("Please input job details and click 'Apply' to show relevant candidates.")

# Footer
st.caption("Output with relevancy score will be shown.")
