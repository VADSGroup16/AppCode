import streamlit as st

# Define the layout of the app
st.set_page_config(layout="wide")

# Use custom CSS to style the app more like the provided image
st.markdown("""
<style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .input-field {
        display: flex;
        flex-direction: column;
        margin-bottom: 10px;
    }
    .input-label {
        font-size: 20px;
        margin-bottom: 5px;
    }
    .apply-btn {
        width: 100px;
        height: 40px;
        font-size: 20px;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Create columns for the input form and the results
col1, col2 = st.columns((2, 3))

# Input form in the first column
with col1:
    st.markdown('<p class="big-font">Job Opening Details</p>', unsafe_allow_html=True)
    role = st.text_input("", placeholder="Role")
    experience = st.text_input("", placeholder="Experience")
    certifications = st.text_input("", placeholder="Certifications")
    skills = st.text_input("", placeholder="Skills")
    apply_button = st.button("Apply", key="apply", help="Click to apply and find relevant candidates")

# Results area in the second column
with col2:
    st.markdown('<p class="big-font">Relevant candidates</p>', unsafe_allow_html=True)
    if apply_button:
        # Logic to search and display candidates
        st.write("Displaying relevant candidates...")  # Replace with actual logic
    else:
        st.write("Apply to see relevant candidates")

# Placeholders for candidate data
candidate_data = []

# Logic for when the Apply button is clicked
if apply_button:
    # Example data
    candidate_data = [
        {"Candidate name": "Alice Johnson", "Contact details": "alice@example.com", "Relevancy score": "89%"},
        {"Candidate name": "Bob Smith", "Contact details": "bob@example.com", "Relevancy score": "85%"},
        # Add more candidate data here
    ]

# Display candidate data in a table
if candidate_data:
    col2.table(candidate_data)
