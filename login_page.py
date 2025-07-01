import streamlit as st
from database import authenticate_user
def navigate_to_page(page_name):
    st.session_state["current_page"] = page_name
    st.rerun()

def login_page():
    st.markdown(
    """
    <style>
    /* Apply background image to main area */
    .main {
        background-image: url("https://img.freepik.com/free-vector/medical-banner-with-healthcare-icons_1017-26805.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    /* Style the login form box */
    div[data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        max-width: 400px;
        margin: auto;
    }

    /* Center the form inside the container */
    section.main > div {
        display: flex;
        justify-content: center;
    }

    /* Adjust form title and home button */
    .form-title {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* Style form inputs and buttons for consistency */
    input, button {
        font-size: 16px !important;
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
        col1,col2=st.columns([1,1])
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
