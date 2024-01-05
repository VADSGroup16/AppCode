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
st.set_page_config(page_title="Recruit VADS")

# Display the header image in the middle of the page
header_image_path = "Header.png"  # Path to the header image file
st.image(header_image_path, width=700)

# Create a two-column layout for the form and candidates table
col1, col2 = st.columns([1, 2])

# Initialize or reset session state
if 'form_data' not in st.session_state:
    st.session_state['form_data'] = {'role': '', 'experience': '', 'skills': ''}
    st.session_state['submitted'] = False

def clear_form():
    st.session_state.form_data = {'role': '', 'experience': '', 'skills': ''}
    st.session_state.submitted = False

with col1:
    with st.container():
        form_data = st.session_state.form_data
        form_data['role'] = st.text_input("Role", value=form_data['role'])
        form_data['experience'] = st.text_input("Experience", value=form_data['experience'])
        form_data['skills'] = st.text_input("Skills", value=form_data['skills'])
        
        apply, clear = st.columns(2)
        if apply.button("Apply"):
            st.session_state.submitted = True
        if clear.button("Clear"):
            clear_form()

with col2:
    if st.session_state.submitted:
        candidates = fetch_candidates(
            form_data['role'], 
            form_data['experience'], 
            form_data['skills']
        )
        st.dataframe(candidates)
    else:
        st.write("Please input job details and click 'Apply' to show relevant candidates.")

st.caption("Output with relevancy score will be shown.")
