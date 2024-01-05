import streamlit as st
import pandas as pd

# Dummy function to simulate candidate retrieval
def fetch_candidates():
    # This would be replaced with your actual data retrieval logic
    return pd.DataFrame({
        'Candidate Name': ['Alice Smith', 'Bob Jones', 'Carol Johnson'],
        'Contact Details': ['alice@example.com', 'bob@example.com', 'carol@example.com'],
        'Relevancy Score': [89, 85, 93]
    })

# Set page configuration
st.set_page_config(layout="wide", page_title="Recruit VADS")

# Display logo in a small column
logo_col, _, title_col = st.columns([1, 10, 20])
with logo_col:
    st.image("recruitment_logo.png", width=100)  # Adjust width as per your logo's aspect ratio

# Add the app title next to the logo
with title_col:
    st.markdown("<h1 style='text-align: center;'>Recruitment Dashboard</h1>", unsafe_allow_html=True)

# Input form and candidate display in columns
form_col, candidates_col = st.columns([2, 3])

# Input form in one column
with form_col:
    with st.form('job_details'):
        role = st.text_input("Role")
        experience = st.number_input("Experience (in years)", min_value=0, max_value=50, step=1)
        certifications = st.text_input("Certifications")
        skills = st.text_input("Skills")
        submit_button = st.form_submit_button("Apply")

# Display relevant candidates in the other column
with candidates_col:
    if submit_button:
        # Retrieve and display candidates
        candidates_df = fetch_candidates()
        st.dataframe(candidates_df.style.format({'Contact Details': lambda x: x.split('@')[0] + '@...'}))
    else:
        st.write("Candidates will appear here once you submit the job details.")

# Ensure the footer is at the bottom of the page
st.write("Page 1 of 1")
