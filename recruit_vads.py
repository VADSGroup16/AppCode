import streamlit as st

# Set page configuration
st.set_page_config(layout="wide", page_title="Recruit VADS")

# Insert logo at the top
logo = "recruit_logo.png"  # Path to the logo image file
process_img = "recruit_process.jpg"  # Path to the process image file

# Place the logo in a container to prevent stretching
with st.container():
    st.image(logo, width=500)  # You can adjust the width as needed

# Create two columns for the job details form and the candidates display
col1, col2 = st.columns([3, 2])

# Column for job details form
with col1:
    st.header("Job Opening Details")
    with st.form(key='job_details'):
        role = st.text_input("Role")
        experience = st.text_input("Experience")
        certifications = st.text_input("Certifications")
        skills = st.text_area("Skills", height=100)
        submit_button = st.form_submit_button("Apply")

# Column for candidates
with col2:
    st.header("Relevant Candidates")
    # Display a message or placeholder before the form is submitted
    if not submit_button:
        st.write("Please enter job details and click 'Apply' to show relevant candidates.")
    # If the form is submitted, you can display the candidates here
    else:
        st.write("Displaying relevant candidates...")

# Place the process image below the columns
st.image(process_img, use_column_width=True)

# The rest of your app logic goes here
# This is where you would process the form input and update the candidates display
