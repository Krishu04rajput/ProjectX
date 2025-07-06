import streamlit as st

st.title("🔍 Viewer Mode")
st.markdown("Below is your Canva viewer.")

st.components.v1.iframe("https://project04x.my.canva.site/making-an-virtual-world", height=700)

if st.button("🔓 Logout"):
    st.session_state.clear()
    st.switch_page("app.py")