import streamlit as st
import pandas as pd

# Initialize session state variables
if 'role' not in st.session_state:
    st.session_state['role'] = ''
if 'experience' not in st.session_state:
    st.session_state['experience'] = ''
if 'certifications' not in st.session_state:
    st.session_state['certifications'] = ''
if 'skills' not in st.session_state:
    st.session_state['skills'] = ''

# Set page configuration
st.set_page_config(page_title="Recruit VADS", layout="wide")

# Header image
st.image("Header.png", use_column_width=True)

# Form for job details
with st.form(key='job_details'):
    cols = st.columns(2)
    cols[0].text_input("Role", key='role')
    cols[1].text_input("Experience", key='experience')
    cols[0].text_input("Certifications", key='certifications')
    cols[1].text_input("Skills", key='skills')
    
    # Buttons side by side
    col1, col2 = st.columns(2)
    with col1:
        submit_button = st.form_submit_button(label='Apply')
    with col2:
        clear_button = st.button(label='Clear')

if clear_button:
    # Clear the form
    st.session_state['role'] = ''
    st.session_state['experience'] = ''
    st.session_state['certifications'] = ''
    st.session_state['skills'] = ''
    st.experimental_rerun()

# Placeholder for candidates list
if submit_button:
    st.write("Displaying relevant candidates...")
    # Assume we fetch candidates here
    candidates = pd.DataFrame({
        'Candidate Name': ['Alice Smith', 'Bob Jones', 'Carol Johnson'],
        'Contact Details': ['alice@example.com', 'bob@example.com', 'carol@example.com'],
        'Relevancy Score': [95, 90, 85]
    })
    st.dataframe(candidates)

st.caption("Output with relevancy score will be shown.")
