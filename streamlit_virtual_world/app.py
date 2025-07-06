import streamlit as st
from supabase_config import client
from utils import check_credentials, go_to_viewer_or_editor

st.set_page_config(page_title="ProjectX Virtual World", layout="centered")

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Step 1: Home Screen with floating logo
if st.session_state.page == 'home':
    st.image("assets/logo.png", width=150)
    st.markdown("<h1 style='text-align:center;'>Welcome to ProjectX</h1>", unsafe_allow_html=True)
    if st.button("🚀 Get Started"):
        st.session_state.page = 'auth'

# Step 2: Auth Screen
elif st.session_state.page == 'auth':
    st.subheader("🔐 Login or Signup")
    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = check_credentials(email, password)
            if user:
                st.success("Login Successful")
                st.session_state.user_email = email
                if email == "k.rajput0542@gmail.com" and password == "Ganesh4.0":
                    go_to_viewer_or_editor()
                else:
                    st.info("Welcome! You don't have Viewer/Editor access.")
                    st.stop()
            else:
                st.error("Invalid credentials")

    with tab2:
        name = st.text_input("Full Name")
        new_email = st.text_input("New Email")
        new_pass = st.text_input("New Password", type="password")
        if st.button("Signup"):
            res = client.auth.sign_up({"email": new_email, "password": new_pass})
            if res:
                st.success("Account created. Please login.")
            else:
                st.error("Signup failed")