import streamlit as st
import pandas as pd
import time

def analysis_page():

    # ---------- NAV ----------
    if st.button("⬅ Back to Home", key="back_from_analysis"):
        st.session_state.page = "home"
        st.rerun()
        st.stop()

    st.title("📊 Crop Yield Intelligence Dashboard")

    # ---------- CREATE HISTORY STORE ----------
    if "history" not in st.session_state:
        st.session_state.history = []

    st.markdown("This dashboard shows insights based on crop yield predictions and inputs.")

    st.markdown("---")

    # =====================================================
    # 1️⃣  SMART SUMMARY CARDS
    # =====================================================
    if st.session_state.history:

        latest = st.session_state.history[-1]

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("🌾 Latest Predicted Yield", f"{latest['yield']:.1f} kg/ha")

        with col2:
            st.metric("🌱 Crop", latest['crop'].capitalize())

        with col3:
            st.metric("📍 Location", latest['district'])

        with col4:
            st.metric("📅 Year", latest['year'])

    else:
        st.info("No predictions stored yet. Make at least one prediction first.")


    # =====================================================
    # 2️⃣  FACTOR INFLUENCE BAR CHART
    # =====================================================
    st.markdown("### 📊 Factor Influence on Crop Yield")

    factor_importance = {
        "Rainfall": 0.30,
        "Temperature": 0.25,
        "Soil pH": 0.15,
        "Nitrogen": 0.12,
        "Phosphorus": 0.10,
        "Potassium": 0.08
    }

    df = pd.DataFrame({
        "Factor": factor_importance.keys(),
        "Importance": factor_importance.values()
    })

    st.bar_chart(df.set_index("Factor"))


    # =====================================================
    # 3️⃣  CROP COMPARISON (RUNS MODEL FOR 4 CROPS)
    # =====================================================
    st.markdown("### 🌾 Crop-wise Yield Comparison (Same Conditions)")

    if st.session_state.history:

        latest = st.session_state.history[-1]

        crop_compare_df = pd.DataFrame({
            "Crop": ["rice", "maize", "chickpea", "cotton"],
            "Predicted Yield (kg/ha)": [
                latest["rice_yield"],
                latest["maize_yield"],
                latest["chickpea_yield"],
                latest["cotton_yield"]
            ]
        })

        crop_compare_df = crop_compare_df.set_index("Crop")

        st.bar_chart(crop_compare_df)

        best_crop = crop_compare_df["Predicted Yield (kg/ha)"].idxmax()

        st.success(f"✅ **Best Performing Crop under current conditions: {best_crop.capitalize()}**")

    else:
        st.info("Run a prediction to view crop-wise comparison.")


    # =====================================================
    # 4️⃣  HISTORICAL TREND OF PREDICTIONS
    # =====================================================
    st.markdown("### 📈 Trend of Your Predictions Over Time")

    if st.session_state.history and len(st.session_state.history) > 1:

        trend_df = pd.DataFrame(st.session_state.history)

        st.line_chart(trend_df[["yield"]])

        st.caption("Shows how predicted yield changed over different inputs.")

    else:
        st.info("Trend chart appears when there are 2 or more predictions.")


    # =====================================================
    # 5️⃣  SOIL pH SUITABILITY
    # =====================================================
    st.markdown("### 🧪 Soil pH Suitability")

    if st.session_state.history:

        pH = latest["pH"]

        if pH < 5.5:
            st.error(f"Soil pH = {pH}. Soil is **acidic** — may reduce nutrient absorption.")
        elif 5.5 <= pH <= 7.5:
            st.success(f"Soil pH = {pH}. pH is **optimal for most crops.**")
        else:
            st.warning(f"Soil pH = {pH}. Soil is **alkaline** — may reduce yield.")

    st.markdown("---")
