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

# Header image
header_image_path = "Header.png"  # Path to the header image file
# Create columns to center the header image
left_spacer, header_col, right_spacer = st.columns([1, 2, 1])
with header_col:
    st.image(header_image_path, use_column_width=True)  # The use_column_width parameter scales the image to fit the column

# Create a two-column layout for the form and candidates table
col1, col2 = st.columns([1, 2])

with col1:
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

with col2:
    if submitted:
        candidates = fetch_candidates(role, experience, certifications, skills)
        st.dataframe(candidates)
    else:
        st.write("Please input job details and click 'Apply' to show relevant candidates.")

st.caption("Output with relevancy score will be shown.")
