import streamlit as st

# Set page configuration
st.set_page_config(layout="wide", page_title="Recruit VADS")

# Insert logo at the top
st.image("recruit_logo.png", use_column_width=True)

# Create columns for the job details form and the candidate display
col1, col2 = st.columns(2)

with col1:
    st.header("Job Opening Details")
    with st.form(key='job_details'):
        role = st.text_input("Role")
        experience = st.text_input("Experience")
        certifications = st.text_input("Certifications")
        skills = st.text_input("Skills")
        submit_button = st.form_submit_button("Apply")
    
    # If the form is submitted, process the input data here
    if submit_button:
        st.success("You have successfully submitted the job details.")

with col2:
    st.header("Relevant Candidates")
    # Initially display a placeholder or instructions
    st.write("Please enter job details and click 'Apply' to show relevant candidates.")

# Assuming the process image should be displayed somewhere on the page
st.image("recruit_process.jpg", use_column_width=True)
# Right column for displaying candidates
with right_column:
    st.header("Relevant Candidates")
    # Placeholder for displaying candidates
    if submitted:
        # After submission, you would normally retrieve and display relevant candidates
        st.write("Displaying relevant candidates...") # replace with actual data retrieval and display

# Below your columns, you can display the footer or additional information
st.write("Output with relevancy score will be shown.")
