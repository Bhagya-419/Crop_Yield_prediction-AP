import streamlit as st
st.markdown("""
<style>

/* =========================
   HOME ACTION BUTTON STYLES
   ========================= */

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

/* Logout button (top-right) */
button[kind="secondary"] {
    height: 40px !important;
    font-size: 15px !important;
}

</style>
""", unsafe_allow_html=True)

def home_page():
    col1, col2 = st.columns([8, 1])

    with col2:
        if st.button("🚪 Logout", key="logout_btn"):
            st.session_state.clear()
            st.session_state.page = "welcome"
            st.rerun()

    st.title(f"👋 Welcome {st.session_state.user_name}")

    # ---------- BUTTONS ----------
    # ---------- ACTION BUTTONS ----------
    btn_left, btn_pred, gap, btn_ana, btn_right = st.columns([1, 2.2, 0.3, 2.2, 1])

    with btn_pred:
        if st.button("🌾 Prediction", key="home_prediction", use_container_width=True):
            st.session_state.page = "prediction"
            st.rerun()
            st.stop()

    with btn_ana:
        if st.button("📊 Analysis", key="home_analysis", use_container_width=True):
            st.session_state.page = "analysis"
            st.rerun()
            st.stop()


    st.markdown("---")

    # ---------- PROJECT INFO BOXES ----------
    st.markdown("### 🚀 About the Project")

    b1, b2, b3 = st.columns(3)

    with b1:
        st.markdown("""
        <div style="
            background:#f8fdf8;
            padding:20px;
            border-radius:14px;
            text-align:center;
            box-shadow:0 4px 12px rgba(0,0,0,0.08);
            height:180px;">
            <h4>🌱 Smart Prediction</h4>
            <p>Uses machine learning to predict crop yield based on soil and weather data.</p>
        </div>
        """, unsafe_allow_html=True)

    with b2:
        st.markdown("""
        <div style="
            background:#f8fdf8;
            padding:20px;
            border-radius:14px;
            text-align:center;
            box-shadow:0 4px 12px rgba(0,0,0,0.08);
            height:180px;">
            <h4>🌦️ Weather Integrated</h4>
            <p>Real-time weather data improves prediction accuracy and reliability.</p>
        </div>
        """, unsafe_allow_html=True)

    with b3:
        st.markdown("""
        <div style="
            background:#f8fdf8;
            padding:20px;
            border-radius:14px;
            text-align:center;
            box-shadow:0 4px 12px rgba(0,0,0,0.08);
            height:180px;">
            <h4>📊 Yield Insights</h4>
            <p>📊 Clearly explains how soil quality, climate conditions, and seasonal factors influence crop yield predictions.</p>
        </div>
        """, unsafe_allow_html=True)
