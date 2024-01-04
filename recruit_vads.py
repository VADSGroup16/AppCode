import streamlit as st
from PIL import Image

# First, define the get_image function
@st.cache
def get_image(image_path):
    return Image.open(image_path)

# Then, immediately set the page configuration
st.set_page_config(layout="wide", page_title="Recruit VADS", page_icon=get_image("recruitment_logo.png"))

# Custom CSS for styling
st.markdown("""
<style>
    .big-font {
        font-size:30px !important;
        color: #ffffff;  /* White color for text */
        font-weight: bold;
    }
    .apply-btn {
        background-color: #0e76a8;  /* A LinkedIn-like blue color */
        color: white;
        padding: 10px 24px;
        margin: 10px 0px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .apply-btn:hover {
        background-color: #0056b3;  /* A darker blue for hover effect */
    }
    .streamlit-input {
        border: 2px solid #0e76a8;
        border-radius: 5px;
    }
    .streamlit-table {
        margin-top: 20px;
    }
    .header-image {
        width: 100%;
        height: auto;
        margin: 10px 0px;
    }
    .stApp {
        background-image: url("/mnt/data/recruitment_process.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
</style>
""", unsafe_allow_html=True)

# Header image
header_image = get_image("recruitment_logo.png")
st.image(header_image, use_column_width='auto')

# Main app interface
col1, col2 = st.columns((1, 2))

# Job Details Form
with col1:
    st.markdown('<p class="big-font">Job Opening Details</p>', unsafe_allow_html=True)
    role = st.text_input("Role", max_chars=50)
    experience = st.text_input("Experience", max_chars=50)
    certifications = st.text_input("Certifications", max_chars=50)
    skills = st.text_input("Skills", max_chars=50)
    apply_button = st.button("Apply", key="apply")

# Candidate Results
with col2:
    st.markdown('<p class="big-font">Relevant Candidates</p>', unsafe_allow_html=True)
    if apply_button:
        st.success("Candidates loading...")

# Footer image
footer_image = get_image("recruitment_process.png")
st.image(footer_image, use_column_width='auto')
