import streamlit as st
import pandas as pd
import joblib
import requests
import os
from home import home_page
from locations import ap_locations  # AP Districts + Mandals/Villages

# ---------------- LOAD MODEL ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "crop_yield_pipeline.pkl")
model = joblib.load(MODEL_PATH)

# ---------------- PREDICTION PAGE ----------------
def prediction_page():

    st.title("🌾 Crop Yield Prediction")
    st.markdown(
        "Predict the expected crop yield (kg/ha) based on **soil conditions, weather data, and crop type**."
    )

    # ---------- BACK BUTTON ----------
    if st.button("⬅ Back to Home", key="back_from_prediction"):
        st.session_state.page = "home"
        st.rerun()
        st.stop()

    # ---------------- SESSION STATE ----------------
    if "temperature" not in st.session_state:
        st.session_state.temperature = 26.0
    if "humidity" not in st.session_state:
        st.session_state.humidity = 70.0
    if "wind_speed" not in st.session_state:
        st.session_state.wind_speed = 2.0

    # ---------------- USER INPUTS ----------------
    crop = st.selectbox("🌱 Select Crop", ["rice", "maize", "chickpea", "cotton"])
    dist_code = 50  # fixed code
    year = st.slider("📅 Year of Cultivation", min_value=2000, max_value=2050, value=2026)

    # ---------------- YEAR INFO ----------------
    if year <= 2005:
        st.warning("🌾 Earlier Farming Phase: Lower yield expected.")
    elif 2006 <= year <= 2022:
        st.info("🚜 Improved Agriculture Phase: Better productivity.")
    else:
        st.error("🌍 Climate Change Phase: Yield depends strongly on weather.")

    area = st.number_input("🌾 Cultivation Area (hectares)", value=1000.0)
    pH = st.slider("🧪 Soil pH", min_value=4.0, max_value=9.0, value=6.5, step=0.1)

    if pH < 5.5:
        st.warning("🧪 Soil is acidic")
    elif 5.5 <= pH <= 7.5:
        st.success("🌱 Soil pH is optimal")
    else:
        st.error("⚠️ Soil is alkaline")

    # ---------------- LOCATION DROPDOWNS ----------------
    st.subheader("📍 Select Location (Andhra Pradesh Only)")

    # District dropdown
    district = st.selectbox("Select District", sorted(ap_locations.keys()))
    
    # Mandal/Village dropdown based on district
    mandal_list = ap_locations[district]
    mandal = st.selectbox("Select Mandal / Village", mandal_list)

    final_place = f"{mandal}, {district}, Andhra Pradesh, India"
    st.info(f"📌 Selected Location: **{mandal}, {district}, Andhra Pradesh**")

    # ---------------- FETCH WEATHER ----------------
    if st.button("🌦️ Fetch Weather"):
        api_key = "YOUR-API-KEY"
        url = "https://api.openweathermap.org/data/2.5/weather"

        weather_fetched = False

        # 1️⃣ Try mandal weather
        try:
            res = requests.get(
                url,
                params={"q": final_place, "appid": api_key, "units": "metric"},
                timeout=20
            )
            res.raise_for_status()
            data = res.json()
            st.session_state.temperature = data["main"]["temp"]
            st.session_state.humidity = data["main"]["humidity"]
            st.session_state.wind_speed = data["wind"]["speed"]
            st.success(f"✔ Weather fetched for {mandal}")
            weather_fetched = True

        except Exception:
            st.warning(f"⚠ Mandal '{mandal}' not found — trying district weather...")

        # 2️⃣ Try district weather if mandal failed
        if not weather_fetched:
            try:
                res = requests.get(
                    url,
                    params={"q": f"{district}, Andhra Pradesh, India",
                            "appid": api_key, "units": "metric"},
                    timeout=20
                )
                res.raise_for_status()
                data = res.json()
                st.session_state.temperature = data["main"]["temp"]
                st.session_state.humidity = data["main"]["humidity"]
                st.session_state.wind_speed = data["wind"]["speed"]
                st.info(f"📍 Using nearest station in {district}")
                weather_fetched = True

            except Exception:
                st.error(f"❌ District weather also unavailable. Using default values.")
                # Use last session state values as fallback
                st.session_state.temperature = st.session_state.temperature
                st.session_state.humidity = st.session_state.humidity
                st.session_state.wind_speed = st.session_state.wind_speed

    # ---------------- WEATHER INPUTS ----------------
    temperature = st.number_input("🌡️ Temperature (°C)", value=st.session_state.temperature)
    humidity = st.number_input("💧 Humidity (%)", value=st.session_state.humidity)
    wind_speed = st.number_input("🌬️ Wind Speed (m/s)", value=st.session_state.wind_speed)
    st.subheader("🧪 Fertilizer Input ")
    nitrogen_fertilizer = st.number_input(
    "Enter Nitrogen Fertilizer (kg/ha)", 
    min_value=0.0, 
    max_value=500.0, 
    value=50.0
    )
    rainfall = st.number_input("🌧️ Rainfall (mm)", value=800.0)
    solar = st.number_input("☀️ Solar Radiation (MJ/m²/day)", value=18.0)

    # ---------------- PREDICT ----------------
    st.markdown("---")
    st.subheader("📈 Model Prediction")

    if st.button("📈 Predict Yield"):
        n_req, p_req, k_req = 30, 15, 25

        input_df = pd.DataFrame([{
            "Dist Code": dist_code,
            "Year": year,
            "State Code": 1,
            "State Name": "Andhra Pradesh",
            "Dist Name": district,
            "Crop": crop,
            "Area_ha": area,
            "N_req_kg_per_ha": n_req,
            "P_req_kg_per_ha": p_req,
            "K_req_kg_per_ha": k_req,
            "Total_N_kg": area * n_req,
            "Total_P_kg": area * p_req,
            "Total_K_kg": area * k_req,
            "Temperature_C": temperature,
            "Humidity_%": humidity,
            "pH": pH,
            "Rainfall_mm": rainfall,
            "Wind_Speed_m_s": wind_speed,
            "Solar_Radiation_MJ_m2_day": solar
        }])

        prediction = model.predict(input_df)[0]

        st.success(f"🌾 Predicted Crop Yield: `{prediction:.2f} kg/ha`")

        if prediction < 2000:
            st.error("⚠️ Yield is low. Crop may be affected by climate or soil conditions.")
        elif prediction < 4000:
            st.warning("⚠️ Yield is moderate. There is scope to improve conditions.")
        else:
            st.success("✅ Yield is high. Conditions look favorable!")

