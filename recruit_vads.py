import streamlit as st

# Set page config to widen the layout
st.set_page_config(layout="wide")

# Display the logo
st.image("recruitment_logo.png")

# Title of the job details form
st.header('Job Opening Details')

# Create a form where the user can input job details
with st.form(key='job_details_form'):
    role = st.text_input(label='Role')
    experience = st.text_input(label='Experience')
    certifications = st.text_input(label='Certifications')
    skills = st.text_area(label='Skills')
    submit_button = st.form_submit_button(label='Apply')

# Check if the form has been submitted
if submit_button:
    # Placeholder for search logic to find relevant candidates
    # In practice, you would replace this with a call to a database or search API
    candidates = [
        {'name': 'Jane Doe', 'contact': 'jane@example.com', 'score': 95},
        # Add more candidate dictionaries here
    ]
    
    # Display candidates in a table
    st.header('Relevant Candidates')
    for candidate in candidates:
        st.write(f"Name: {candidate['name']}, Contact: {candidate['contact']}, Relevancy Score: {candidate['score']}")
