
import streamlit as st
import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT PRIMARY KEY, password TEXT)')
    # Check if the username already exists
    c.execute('SELECT * FROM userstable WHERE username = ?', (username,))
    if c.fetchone():
        conn.close()
        return False  # Username exists
    else:
        c.execute('INSERT INTO userstable(username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return True


st.title("Sign Up Page")

new_user = st.text_input("New Username")
new_password = st.text_input("New Password", type="password")

if st.button("Create Account"):
    if new_user and new_password:
        success = add_user(new_user, hash_password(new_password))
        if success:
            st.success("Account created successfully!")
            st.switch_page("pages/login.py")
        else:
            st.error("Username already exists. Please choose another one.")
    else:
        st.error("Please provide both username and password")
