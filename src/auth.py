import streamlit as st
import pandas as pd
import os

USERS_FILE = os.path.join("data", "users.csv")

def load_users():
    if not os.path.exists(USERS_FILE):
        df = pd.DataFrame(columns=["name", "username", "password"])
        df.to_csv(USERS_FILE, index=False)
    return pd.read_csv(USERS_FILE)

def signup():
    st.subheader("📝 Sign Up")

    name = st.text_input("Full Name", key="signup_name")
    username = st.text_input("Email or Username", key="signup_user")
    password = st.text_input("Password", type="password", key="signup_pass")

    if st.button("Create Account", key="signup_btn"):
        users = load_users()

        if username in users["username"].values:
            st.error("User already exists")
            return

        new_user = pd.DataFrame(
            [[name, username, password]],
            columns=["name", "username", "password"]
        )
        users = pd.concat([users, new_user], ignore_index=True)
        users.to_csv(USERS_FILE, index=False)

        st.success("✅ Account created! Please login.")

        # 🔥 FIXED NAVIGATION
        st.session_state.page = "welcome"
        st.session_state.auth_mode = "login"

        st.rerun()


def login():
    st.subheader("🔐 Login")

    username = st.text_input("Email or Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login", key="login_btn"):
        users = load_users()
        user = users[
            (users["username"] == username) &
            (users["password"] == password)
        ]

        if not user.empty:
            st.session_state.logged_in = True
            st.session_state.user_name = user.iloc[0]["name"]
            st.session_state.page = "home"   # 🔥 redirect to home
            st.success("Login successful")
            st.rerun()

        else:
            st.error("Invalid credentials")
