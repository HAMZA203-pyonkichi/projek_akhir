import streamlit as st
import pandas as pd
import joblib

# --- Page Config ---
st.set_page_config(page_title="Prediksi Harga Rumah - TIM KAMI", page_icon="🏠", layout="centered")

# --- Load model ---
model = joblib.load("model/linreg_model.pkl")

# --- Custom CSS with Blue-White Gradient Background ---
st.markdown("""
    <style>
        html, body, .stApp {
            height: 100%;
            margin: 0;
            padding: 0;
            background: linear-gradient(to bottom, #1e3a8a, #ffffff);
            color: #0f172a;
            font-family: 'Segoe UI', sans-serif;
        }

        .title {
            color: #ffffff;
            text-align: center;
            font-size: 38px;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .subheader {
            text-align: center;
            color: #334155;
            font-size: 18px;
            margin-bottom: 35px;
        }

        label, .st-bb {
            color: #1e293b !important;
        }

        .footer {
            text-align: center;
            color: #64748b;
            margin-top: 40px;
            font-size: 13px;
        }

        .prediction-box {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-top: 30px;
        }

        .stButton > button {
            background-color: #2563eb;
            color: white;
            border: None;
            padding: 0.6em 1.2em;
            border-radius: 8px;
            font-weight: bold;
            transition: 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #1d4ed8;
        }

        .stNumberInput input {
            background-color: #f8fafc;
        }

        .stSelectbox div {
            background-color: #f8fafc;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='title'>🏠 Prediksi Harga Rumah - TIM KAMI</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Isi data properti di bawah untuk memprediksi estimasi harga rumah</div>", unsafe_allow_html=True)

# --- Input Form ---
with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        crim = st.number_input("CRIM", min_value=0.0, step=0.1)
        zn = st.number_input("ZN", min_value=0.0, step=1.0)
        indus = st.number_input("INDUS", min_value=0.0, step=0.1)
        chas = st.selectbox("CHAS (Dekat Sungai)", [0, 1])
        nox = st.number_input("NOX", min_value=0.0, step=0.01)
        rm = st.number_input("RM (Jumlah Kamar)", min_value=0.0, step=0.1)

    with col2:
        age = st.number_input("AGE (Usia Bangunan)", min_value=0.0, step=0.1)
        dis = st.number_input("DIS (Jarak ke Pusat)", min_value=0.0, step=0.1)
        rad = st.number_input("RAD (Akses Jalan)", min_value=0.0, step=1.0)
        tax = st.number_input("TAX (Pajak)", min_value=0.0, step=1.0)
        ptratio = st.number_input("PTRATIO (Rasio Siswa/Guru)", min_value=0.0, step=0.1)
        b = st.number_input("B (Indeks B)", min_value=0.0, step=1.0)
        lstat = st.number_input("LSTAT (Status Sosial)", min_value=0.0, step=0.1)

    submitted = st.form_submit_button("🔍 Prediksi Harga")

# --- Prediction Result ---
if submitted:
    input_data = pd.DataFrame([[crim, zn, indus, chas, nox, rm,
                                age, dis, rad, tax, ptratio, b, lstat]],
                              columns=['crim', 'zn', 'indus', 'chas', 'nox', 'rm',
                                       'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat'])

    prediction = model.predict(input_data)[0]

    st.markdown(f"""
        <div class='prediction-box'>
            <h3 style='color:#10b981;'>💰 Estimasi Harga Rumah</h3>
            <h1 style='color:#0f766e;'>${prediction * 1000:,.2f}</h1>
        </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>✨ Aplikasi oleh Tim STIKOM | TIM KAMI  Housing 2025</div>", unsafe_allow_html=True)
