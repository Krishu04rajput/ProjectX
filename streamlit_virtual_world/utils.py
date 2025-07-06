import streamlit as st
from supabase_config import client

def check_credentials(email, password):
    try:
        user = client.auth.sign_in_with_password({"email": email, "password": password})
        return user
    except:
        return None

def go_to_viewer_or_editor():
    choice = st.radio("Select Mode", ["Viewer", "Editor"])
    if choice == "Viewer":
        st.switch_page("pages/1_Viewer.py")
    elif choice == "Editor":
        st.switch_page("pages/2_Editor.py")