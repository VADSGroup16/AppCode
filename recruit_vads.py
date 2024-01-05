import streamlit as st
import pandas as pd

# Function to simulate fetching candidate data
def fetch_candidates(role, experience, skills):
    return pd.DataFrame({
        'Candidate Name': ['Alice Smith', 'Bob Jones', 'Carol Johnson'],
        'Contact Details': ['alice@example.com', 'bob@example.com', 'carol@example.com'],
        'Relevancy Score': [95, 90, 88]
    })

# Set page configuration
st.set_page_config(page_title="Recruit VADS", layout="wide")

header_image_path = "Header.png"  # Adjust the path as necessary
st.image(header_image_path, width=700)

col1, col2 = st.columns([1, 2])

# Define session state keys
if 'role' not in st.session_state:
    st.session_state.role = ''
if 'experience' not in st.session_state:
    st.session_state.experience = ''
if 'skills' not in st.session_state:
    st.session_state.skills = ''
if 'clear_form' not in st.session_state:
    st.session_state.clear_form = False
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

with col1:
    with st.container():
        role = st.text_input("Role", value=st.session_state.role)
        experience = st.text_input("Experience", value=st.session_state.experience)
        skills = st.text_input("Skills", value=st.session_state.skills)

        apply, clear = st.columns(2)
        if apply.button("Apply"):
            st.session_state.submitted = True
        if clear.button("Clear"):
            st.session_state.clear_form = not st.session_state.clear_form

# Reset the form fields if clear_form is toggled
if st.session_state.clear_form:
    st.session_state.role = ''
    st.session_state.experience = ''
    st.session_state.skills = ''
    st.session_state.submitted = False
    st.experimental_rerun()

with col2:
    if st.session_state.submitted:
        candidates = fetch_candidates(st.session_state.role, st.session_state.experience, st.session_state.skills)
        st.dataframe(candidates)
    else:
        st.write("Please input job details and click 'Apply' to show relevant candidates.")

st.caption("Output with relevancy score will be shown.")
