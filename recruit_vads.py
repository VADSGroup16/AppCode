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
st.set_page_config(page_title="Recruit VADS", layout="wide")

# Display the header image in the middle of the page
header_image_path = "Header.png"  # Path to the header image file
st.image(header_image_path, use_column_width=True)

# Create a container for the form and candidates table
with st.container():
    # Using columns to manage the layout of the form
    form_col1, form_col2, form_col3 = st.columns([1, 1, 2])
    with form_col1:
        role = st.text_input("Role", key="role")
    with form_col2:
        experience = st.text_input("Experience", key="experience")
    with form_col3:
        certifications = st.text_input("Certifications", key="certifications")
        skills = st.text_input("Skills", key="skills")

    # Buttons for applying and clearing form
    apply_col, clear_col = st.columns(2)
    with apply_col:
        if st.button("Apply"):
            # Simulate fetching data (replace with actual logic)
            candidates = fetch_candidates()
            # Display candidates in a dataframe
            st.dataframe(candidates)
    with clear_col:
        if st.button("Clear"):
            # Clear the input values
            for key in st.session_state.keys():
                st.session_state[key] = ""

# Ensure the footer is at the bottom of the page
st.caption("Output with relevancy score will be shown.")

# This will prevent Streamlit from automatically rerunning the script on interaction with inputs
st.stop()
