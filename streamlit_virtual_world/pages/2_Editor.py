import streamlit as st

st.title("🛠️ Editor Mode")

editor_mode = st.radio("Choose Editor:", ["Canva", "Replit"])

if editor_mode == "Canva":
    st.components.v1.iframe("https://www.canva.com/design/DAGgflx2YY4", height=700)
elif editor_mode == "Replit":
    st.components.v1.iframe("https://replit.com/@yourusername/yourproject?embed=true", height=700)

if st.button("🔓 Logout"):
    st.session_state.clear()
    st.switch_page("app.py")