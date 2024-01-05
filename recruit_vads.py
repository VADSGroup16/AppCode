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


# Function to get base64 of an image
def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Convert the header image to base64
header_image_base64 = get_image_base64("Header.png")

# Display the header image with specific width and height
st.markdown(
    f'<div style="text-align: center;"><img src="data:image/png;base64,{header_image_base64}" style="width: 400px; height: 150px;"></div>', 
    unsafe_allow_html=True
)

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

        role = st.text_input("Role", value=st.session_state['role'])
        experience = st.text_input("Experience", value=st.session_state['experience'])
        certifications = st.text_input("Certifications", value=st.session_state['certifications'])
        skills = st.text_input("Skills", value=st.session_state['skills'])
        
        # Place Apply and Clear buttons side by side
        apply, clear = st.columns(2)
        if apply.button("Apply"):
            st.session_state['submitted'] = True
        if clear.button("Clear"):
            st.session_state['role'] = ''
            st.session_state['experience'] = ''
            st.session_state['certifications'] = ''
            st.session_state['skills'] = ''
            st.session_state['submitted'] = False

# The right column will display the candidates
with col2:
    if st.session_state.get('submitted'):
        candidates = fetch_candidates(
            st.session_state['role'], 
            st.session_state['experience'], 
            st.session_state['certifications'], 
            st.session_state['skills']
        )
        st.dataframe(candidates)
    else:
        st.write("Please input job details and click 'Apply' to show relevant candidates.")

st.caption("Output with relevancy score will be shown.")
