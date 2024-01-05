import streamlit as st

# Set page config to have a wide layout
st.set_page_config(layout="wide")

# Using columns to create a side-by-side layout for the form and candidate list
left_column, right_column = st.columns([2, 3])

# Left column for user input
with left_column:
    st.header("Job Opening Details")
    with st.form(key='job_details'):
        role = st.text_input("Role")
        experience = st.text_input("Experience")
        certifications = st.text_input("Certifications")
        skills = st.text_input("Skills")
        submitted = st.form_submit_button("Apply")
    if submitted:
        st.success("Details submitted successfully!")

# Right column for displaying candidates
with right_column:
    st.header("Relevant Candidates")
    # Placeholder for displaying candidates
    if submitted:
        # After submission, you would normally retrieve and display relevant candidates
        st.write("Displaying relevant candidates...") # replace with actual data retrieval and display

# Below your columns, you can display the footer or additional information
st.write("Output with relevancy score will be shown.")
