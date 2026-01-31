
import streamlit as st
import os

st.set_page_config(page_title="Government Scheme Chatbot", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

if st.session_state.logged_in:
    st.switch_page("pages/chat.py")
else:
    st.switch_page("pages/login.py")
