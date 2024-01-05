import streamlit as st
import pandas as pd
import requests  # For communicating with backend server (if applicable)

st.set_page_config(page_title="Recruit VADS", layout="wide")

with st.sidebar:
    st.title("Job Details")
    role = st.text_input("Role")
    experience = st.text_input("Experience")
    certifications = st.text_input("Certifications")
    skills = st.text_input("Skills")
    apply_button = st.button("Apply", key="apply_sidebar")  # Note the indentation

def process_job_details(role, experience, certifications, skills):
    # Replace this with your logic to retrieve relevant candidates
    # If using a backend server, make requests to it here
    # For now, create a sample candidate dataframe
    candidates_df = pd.DataFrame({
        "Name": ["John Doe", "Jane Smith", "Bob Johnson"],
        "Email": ["john@example.com", "jane@example.com", "bob@example.com"],
        "Relevancy Score": [85, 92, 78]
    })
    return candidates_df

with st.container():
    st.title("Job Opening Details")
    # Display job details based on user input (replace with actual data)
    st.write("Role:", role)
    st.write("Experience:", experience)

    if apply_button:
        candidates_df = process_job_details(role, experience, certifications, skills)
        st.table(candidates_df)

    st.button("Apply", key="apply_main")  # Note the indentation

if __name__ == "__main__":
    st.run()
