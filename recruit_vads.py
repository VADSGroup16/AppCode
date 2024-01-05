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

# Using the session state to store and reset form values
def reset_form():
    for key in ['role', 'experience', 'certifications', 'skills']:
        st.session_state[key] = ''

# Check if form has been submitted
submitted = False

with col1:
    # Using container to keep the form compact
    with st.container():
        role = st.text_input("Role", key='role')
        experience = st.text_input("Experience", key='experience')
        certifications = st.text_input("Certifications", key='certifications')
        skills = st.text_input("Skills", key='skills')

        # Form buttons
        col_apply, col_clear = st.columns([1, 1])
        if col_apply.button("Apply"):
            submitted = True
        if col_clear.button("Clear"):
            reset_form()

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
