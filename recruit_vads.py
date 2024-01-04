import streamlit as st

# Define the layout of the app and set a title
st.set_page_config(layout="wide", page_title="Recruit VADS")

# Custom CSS to inject into Streamlit
st.markdown("""
<style>
    .big-font {
        font-size:30px !important;
        color: #0e76a8;  /* A LinkedIn-like blue color */
        font-weight: bold;
    }
    .apply-btn {
        background-color: #ff6347;  /* A tomato-like color */
        color: white;
        padding: 10px 24px;
        margin: 10px 0px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .apply-btn:hover {
        background-color: #ff4500;
    }
    .streamlit-input {
        border: 2px solid #0e76a8;
        border-radius: 5px;
    }
    .streamlit-table {
        margin-top: 20px;
    }
    .recruit-image {
        max-height: 300px;
    }
</style>
""", unsafe_allow_html=True)

# Header with image
st.image('recruitment_process.jpg', use_column_width=True)  # Replace 'recruitment_image.jpg' with your image file

# Create columns for the input form and the results
col1, col2 = st.columns((1, 2))

# Input form in the first column
with col1:
    st.markdown('<p class="big-font">Job Opening Details</p>', unsafe_allow_html=True)
    role = st.text_input("", placeholder="Role", key="role", help="Enter the job role")
    experience = st.text_input("", placeholder="Experience", key="experience", help="Enter the required experience")
    certifications = st.text_input("", placeholder="Certifications", key="certifications", help="Enter the required certifications")
    skills = st.text_input("", placeholder="Skills", key="skills", help="Enter the required skills")
    if st.button("Apply", key="apply", help="Click to apply and find relevant candidates", on_click=None):
        st.markdown('<p class="big-font" style="color: green;">Applied Successfully!</p>', unsafe_allow_html=True)

# Results area in the second column
with col2:
    st.markdown('<p class="big-font">Relevant candidates</p>', unsafe_allow_html=True)
    if st.session_state.get("apply", False):  # Check if the 'Apply' button was clicked
        # Example static data (you would replace this with actual search results)
        candidate_data = [
            {"Candidate name": "Alice Johnson", "Contact details": "alice@example.com", "Relevancy score": "89%"},
            {"Candidate name": "Bob Smith", "Contact details": "bob@example.com", "Relevancy score": "85%"},
            # Add more candidate data here
        ]
        st.table(candidate_data)
    else:
        st.write("Apply to see relevant candidates")
