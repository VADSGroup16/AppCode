import streamlit as st

# Set page config to widen the layout
st.set_page_config(layout="wide")

# Display the logo and header side-by-side
col1, col2 = st.columns([1, 3])
with col1:
    st.image("Recruitment_logo.png", width=200)  # Adjust path and width as needed
with col2:
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
