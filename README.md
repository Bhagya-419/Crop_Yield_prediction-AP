🌾 Crop Yield Prediction System
📌 Project Overview

This project is a Crop Yield Prediction System built using Machine Learning and Streamlit.
It predicts the expected crop yield (kg/ha) for major crops in Andhra Pradesh based on soil, weather, and agricultural parameters.
The system is designed to support farmers, students, and decision-makers with data-driven insights.

🎯 Objectives

Predict crop yield accurately using ML

Integrate real-time weather data

Restrict location selection to Andhra Pradesh

Provide a simple, interactive, and user-friendly interface

Demonstrate practical use of ML in agriculture

🌱 Crops Supported

Rice

Maize

Chickpea

Cotton

📥 Input Parameters

Crop type

Year of cultivation

Cultivation area (hectares)

Soil pH

Weather parameters

Temperature

Humidity

Rainfall

Wind speed

Fertilizer input (Nitrogen – for demonstration)

Location (District → Mandal dropdowns)

🌦️ Weather Data Handling

Weather data is fetched using OpenWeatherMap API

If mandal weather is unavailable:

District weather is used automatically

If both fail:

Previously stored values are used as fallback
✔️ Ensures uninterrupted prediction

🧠 Machine Learning Model

Algorithm: Random Forest Regressor

Pipeline: Preprocessing + Model

Target Variable: Crop Yield (kg/ha)

Features: Weather, soil, nutrients, crop, year, area

🖥️ Tech Stack

Frontend: Streamlit

Backend: Python

ML: Scikit-learn

Weather API: OpenWeatherMap

Data Handling: Pandas, Joblib

📊 Features

Dynamic district → mandal dropdowns

Real-time weather integration

Smart weather fallback mechanism

Fertilizer input for presentation credibility

Clean UI with clear insights

Ready for future enhancements like charts & history tracking

🚀 How to Run the Project

Clone the repository

Install dependencies

pip install -r requirements.txt


Run the app

streamlit run src/app.py


Open the browser and start predicting 🌾

🔮 Future Enhancements

Store prediction history

Add dynamic analysis charts

Include soil type classification

Recommendation system for fertilizers

Mobile-friendly UI

👩‍🎓 Academic Note

This project was developed as a college mini-project and later enhanced with real-world features to improve practicality and presentation quality.

❤️ Acknowledgements

OpenWeatherMap API

Streamlit Community

Faculty & mentors for guidance
