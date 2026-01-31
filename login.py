
import streamlit as st
import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchone()
    conn.close()
    return data

st.title("Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    hashed_pswd = hash_password(password)
    user = login_user(username, hashed_pswd)
    if user:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success(f"Welcome {username}!")
        st.switch_page("pages/chat.py")
    else:
        st.error("Incorrect username or password")

if st.button("Don't have an account? Sign up here"):
    st.switch_page("pages/signup.py")
