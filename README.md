# 🌾 Crop Yield Prediction System

A Machine Learning-based web application that predicts **crop yield (kg/ha)** for major crops in Andhra Pradesh using soil, weather, and agricultural parameters.
The system is designed to help farmers, students, and researchers make **data-driven decisions**.

---

## 🎯 Objectives

* Predict crop yield accurately using Machine Learning
* Integrate real-time weather data
* Restrict location selection to Andhra Pradesh
* Provide a simple and user-friendly interface
* Demonstrate practical ML application in agriculture

---

## 🌱 Supported Crops

* Rice
* Maize
* Chickpea
* Cotton

---

## 📥 Input Parameters

* Crop Type
* Year of Cultivation
* Area (hectares)
* Soil pH
* Temperature
* Humidity
* Rainfall
* Wind Speed
* Nitrogen (Fertilizer input)
* Location (District → Mandal dropdowns)

---

## 🌦️ Weather Data Handling

* Uses **OpenWeatherMap API**
* If mandal weather is unavailable → district data is used
* If both fail → fallback stored values are used
* Ensures **continuous prediction without interruption**

---

## 🧠 Machine Learning Model

* Algorithm: Random Forest Regressor
* Pipeline: Preprocessing + Model
* Target: Crop Yield (kg/ha)
* Features:

  * Weather data
  * Soil properties
  * Crop type
  * Year
  * Area

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Machine Learning

* Scikit-learn

### Data Handling

* Pandas
* Joblib

### API

* OpenWeatherMap

---

## 📂 Project Structure

```
CROP_PREDICTIONLATEST/
│
├── data/
│   └── crop_data.csv
│
├── models/
│   └── crop_yield_pipeline.pkl
│
├── notebooks/
│   ├── crop_prediction.ipynb
│   └── crop_yield_pipeline.pkl
│
├── src/
│   │
│   ├── __pycache__/
│   │   ├── analysis.cpython-311.pyc
│   │   ├── analysis.cpython-312.pyc
│   │   ├── auth.cpython-311.pyc
│   │   ├── auth.cpython-312.pyc
│   │   ├── home.cpython-311.pyc
│   │   ├── home.cpython-312.pyc
│   │   ├── locations.cpython-312.pyc
│   │   ├── prediction.cpython-311.pyc
│   │   └── prediction.cpython-312.pyc
│   │
│   ├── data/
│   │   └── users.csv
│   │
│   ├── analysis.py
│   ├── app.py
│   ├── auth.py
│   ├── home.py
│   ├── locations.py
│   └── prediction.py
│
└── requirements.txt
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Bhagya-419/Crop_Yield_Prediction.git
cd Crop_Yield_Prediction
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```bash
streamlit run src/app.py
```

---

### 4️⃣ Open in Browser

```
http://localhost:8501
```

---

## 📊 Features

* Dynamic district → mandal dropdowns
* Real-time weather integration
* Smart fallback mechanism
* Clean and interactive UI
* Ready for enhancements (charts, tracking)

---

## 🔮 Future Enhancements

* Store prediction history
* Add visualization charts
* Soil classification system
* Fertilizer recommendation system
* Mobile-friendly UI

---

## 👩‍🎓 Academic Note

This project was developed as a **college mini-project** and enhanced with real-world features for better usability and presentation.

---

## ❤️ Acknowledgements

* OpenWeatherMap API
* Streamlit Community
* Faculty & Mentors

---

## 👩‍💻 Developed By

**Bhagya Lakshmi**
