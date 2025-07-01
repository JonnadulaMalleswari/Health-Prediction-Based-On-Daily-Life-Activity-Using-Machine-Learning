import streamlit as st
from database import authenticate_user
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name
    st.rerun()

def login_page():
    st.markdown(
    """
    <style>
    .main {
        background-image: url("https://img.freepik.com/free-vector/medical-banner-with-healthcare-icons_1017-26805.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    /* Tighter and centered login form */
    div[data-testid="stForm"] {
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(0,0,0,0.2);
        width: 400px;
        margin: auto;
    }

    /* Align title and home icon */
    div[data-testid="column"] h1 {
        display: inline-block;
        font-size: 28px;
        vertical-align: middle;
    }

    div[data-testid="column"] button {
        display: inline-block;
        vertical-align: middle;
        margin-top: 0.3rem;
        margin-left: 10px;
        height: 2.5rem;
    }

    /* Input field spacing */
    .stTextInput {
        margin-bottom: 1rem;
    }

    /* Equal width buttons */
    div[data-testid="column"] button[kind="primary"] {
        width: 100%;
    }
    </style>
    """,
    
    unsafe_allow_html=True
)

  
    
    col1,col2,col3 = st.columns([2,5,1])
    with col2.form(key="login_form"):
        # Title
        col1,col2=st.columns([5,2])
        col1.title("Login Here !!!")
        if col2.form_submit_button("🏚️"):
            navigate_to_page("home")

        # Email and Password inputs
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        # Submit button inside the form
        col1,col2=st.columns([1,2])
        with col1:
            if st.form_submit_button("Login 🔐",type='primary'):
                if authenticate_user(email, password):
                    st.success(f"Login successful.")
                    st.session_state["logged_in"] = True
                    st.session_state["current_user"] = email

                    navigate_to_page("user_home")
                else:
                    st.error("Invalid email or password.")
        with col2:
            if st.form_submit_button("Create account👤",type='primary'):
                navigate_to_page("signup")
