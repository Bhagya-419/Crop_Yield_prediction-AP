import streamlit as st
from auth import login, signup
from prediction import prediction_page
from analysis import analysis_page
from home import home_page

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Crop Yield App", layout="centered")

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = None

# ---------------- CSS ----------------
st.markdown("""
<style>
.hero {
    position: relative;
    border-radius: 18px;
    overflow: hidden;
    margin-bottom: 40px;
}
.hero img {
    width: 100%;
    height: 340px;
    object-fit: cover;
}
.hero::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(
        rgba(0,0,0,0.45),
        rgba(0,0,0,0.25)
    );
}
.hero-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    color: white;
    z-index: 2;
    width: 90%;
}
.hero-title {
    font-size: 48px;
    font-weight: 800;
    text-shadow: 0 6px 14px rgba(0,0,0,0.6);
}
.hero-subtitle {
    font-size: 20px;
    text-shadow: 0 4px 10px rgba(0,0,0,0.5);
}
            
/* Base button styling */
button {
    border-radius: 14px !important;
    height: 52px !important;
    font-size: 17px !important;
    font-weight: 600 !important;
    transition: all 0.25s ease-in-out !important;
}

/* Hover effect */
button:hover {
    background: linear-gradient(
        135deg,
        #e8f5e9,
        #c8e6c9
    ) !important;
    color: #1b5e20 !important;
    transform: translateY(-3px) scale(1.01);
    box-shadow: 0 10px 25px rgba(46, 125, 50, 0.25) !important;
    border: 1px solid #a5d6a7 !important;
}

/* Click effect */
button:active {
    transform: scale(0.98);
}

</style>
""", unsafe_allow_html=True)

# =================================================
# 🌾 WELCOME PAGE
# =================================================
if st.session_state.page == "welcome":

    st.markdown("""
    <div class="hero">
        <img src="https://media.istockphoto.com/id/507512896/photo/fertile-agricultural-field-of-organic-crops-in-california.jpg?s=612x612&w=0&k=20&c=x5VzUR71-uqYHHd0zNfyEZ48w8Sc5noM_mmqTXrW01U=">
        <div class="hero-text">
            <div class="hero-title">🌾ANNADATA MITRA🌾</div>
            <div class="hero-subtitle">
                Farmer's Friend For Better Yield Prediction Using Machine Learning Algorithm and real-time weather data
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, gap, col3, col4 = st.columns([1, 2, 0.5, 2, 1])

    with col2:
        if st.button("🔐 Login", key="welcome_login", use_container_width=True):
            st.session_state.auth_mode = "login"

    with col3:
        if st.button("📝 Sign Up", key="welcome_signup", use_container_width=True):
            st.session_state.auth_mode = "signup"

    st.markdown("---")

    if st.session_state.auth_mode == "login":
        login()

    elif st.session_state.auth_mode == "signup":
        signup()

# =================================================
# 🏠 HOME PAGE
# =================================================
elif st.session_state.page == "home" and st.session_state.logged_in:
    home_page()

# =================================================
# 🌾 PREDICTION PAGE
# =================================================
elif st.session_state.page == "prediction" and st.session_state.logged_in:
    prediction_page()

# =================================================
# 📊 ANALYSIS PAGE
# =================================================
elif st.session_state.page == "analysis" and st.session_state.logged_in:
    analysis_page()
