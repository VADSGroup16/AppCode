import streamlit as st
import pandas as pd

# Function to simulate fetching candidate data
def fetch_candidates(role, experience, skills):
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
st.image(header_image_path, width=700)

# Create a two-column layout for the form and candidates table
col1, col2 = st.columns([1, 2])

# Initialize session states for form fields and submission status
if 'role' not in st.session_state:
    st.session_state['role'] = ''
if 'experience' not in st.session_state:
    st.session_state['experience'] = ''
if 'skills' not in st.session_state:
    st.session_state['skills'] = ''
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

with col1:
    with st.container():
        role = st.text_input("Role", value=st.session_state['role'])
        experience = st.text_input("Experience", value=st.session_state['experience'])
        skills = st.text_input("Skills", value=st.session_state['skills'])
        
        apply, clear = st.columns(2)
        if apply.button("Apply"):
            st.session_state['submitted'] = True
        if clear.button("Clear"):
            st.session_state['role'] = ''
            st.session_state['experience'] = ''
            st.session_state['skills'] = ''
            st.session_state['submitted'] = False  # Also reset the submission state

with col2:
    if st.session_state['submitted']:
        candidates = fetch_candidates(
            st.session_state['role'], 
            st.session_state['experience'], 
            st.session_state['skills']
        )
        st.dataframe(candidates)
    else:
        st.write("Please input job details and click 'Apply' to show relevant candidates.")

st.caption("Output with relevancy score will be shown.")
