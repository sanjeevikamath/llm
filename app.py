import streamlit as st
from main import main_app, login_page

if "auth_token" not in st.session_state:
    login_page()
elif not hasattr(st.session_state, "logged_in") or not st.session_state.logged_in:
    login_page()
else:
    main_app()
