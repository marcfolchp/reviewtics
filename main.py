import streamlit as st

# Configure the page
st.set_page_config(page_title="ReviewTics Login", page_icon="🔒")

# Inject custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f8f0fc;  /* Light purple background */
        color: #4b0082;  /* Indigo text */
        font-family: 'Arial', sans-serif;
    }
    .container {
        max-width: 400px;
        margin: 2em auto;
        padding: 2em;
        background: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .title {
        font-size: 1.5em;
        font-weight: bold;
        margin-bottom: 1em;
    }
    .stTextInput>div>div>input {
        border: 1px solid #d4a1f9;
        border-radius: 5px;
        padding: 0.5em;
    }
    .stButton>button {
        background-color: #dcd3ff; /* Soft purple button */
        color: #4b0082;
        border: none;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-size: 1rem;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #c7b3f9;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML container for the login form
st.markdown(
    """
    <div class="container">
        <div class="title">Login</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Login form inputs
username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", placeholder="Enter your password", type="password")

# Login button
if st.button("Login"):
    st.info("This is a mock login button. Add functionality as needed!")

# Footer or additional note
st.markdown(
    """
    <div style="text-align: center; margin-top: 2em; font-size: 0.9em;">
        © 2024 ReviewTics | All rights reserved.
    </div>
    """,
    unsafe_allow_html=True,
)