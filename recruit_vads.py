import streamlit as st
from PIL import Image
import base64

# Function to get base64 of an image
def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set page config
st.set_page_config(layout="wide")

# Convert the uploaded image to base64
background_image_base64 = get_image_base64("recruitment_process")

# Custom CSS to set the background image
background_style = f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{background_image_base64}");
    background-size: cover;
}}
</style>
"""

# Inject custom CSS with the background
st.markdown(background_style, unsafe_allow_html=True)

# Continue with the rest of your Streamlit app code
st.title('Recruitment Dashboard')

# Using columns to create a side-by-side layout for the form and candidate list
form_col, candidates_col = st.columns(2)

with form_col:
    st.header('Job Opening Details')
    # Create a form where the user can input job details
    with st.form(key='job_details_form'):
        role = st.text_input(label='Role')
        experience = st.text_input(label='Experience')
        certifications = st.text_input(label='Certifications')
        skills = st.text_area(label='Skills', height=100)
        submit_button = st.form_submit_button(label='Apply')

with candidates_col:
    st.header('Relevant Candidates')
    # Display a placeholder for candidate data
    st.table([{'Candidate Name': '---', 'Contact Details': '---', 'Relevancy Score': '---'}])

# Check if the form has been submitted
if submit_button:
    # Placeholder for search logic to find relevant candidates
    # Here you would typically fetch and process data from a database or API
    candidates = [
        {'Candidate Name': 'Alice Smith', 'Contact Details': 'alice@example.com', 'Relevancy Score': 89},
        {'Candidate Name': 'Bob Brown', 'Contact Details': 'bob@example.com', 'Relevancy Score': 85},
        # ... add more candidates as needed
    ]
    
    # Update the candidate list with real data
    candidates_col.table(candidates)
