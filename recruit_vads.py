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
left_col, mid_col, right_col = st.columns([1, 2, 1])
with mid_col:
    st.image(header_image_path, use_column_width=True)

# Create a two-column layout for the form and candidates table
col1, col2 = st.columns([3, 2])

with col1:
    with st.form(key='job_details_form'):
        role = st.text_input("Role")
        experience = st.text_input("Experience")
        certifications = st.text_input("Certifications")
        skills = st.text_input("Skills")
        submit_button = st.form_submit_button("Apply")

if submit_button:
    # Simulate fetching data based on form input (this would be your actual data retrieval logic)
    candidates = fetch_candidates(role, experience, certifications, skills)
    # Create a dataframe and display it on the right column
    col2.dataframe(candidates)
else:
    # Before form submission, show instructions in the right column
    col2.write("Please input job details and click 'Apply' to show relevant candidates.")

# Footer
st.caption("Output with relevancy score will be shown.")
