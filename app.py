import streamlit as st
import requests

# Configuración de la API de DataRobot
DATAROBOT_API_KEY = st.secrets["DATAROBOT_API_KEY"]
DATAROBOT_DEPLOYMENT_ID = st.secrets["DATAROBOT_DEPLOYMENT_ID"]
DATAROBOT_HOST = st.secrets["DATAROBOT_HOST"]  # Ejemplo: "https://app.datarobot.com"
PREDICTION_ENDPOINT = f"{DATAROBOT_HOST}/api/v2/deployments/{DATAROBOT_DEPLOYMENT_ID}/predictions"

# Estilo de la página
st.set_page_config(page_title="🚗 Predicción de Servicio Vehicular", layout="wide")
st.markdown(
    """
    <style>
    .title {
        font-size: 50px;
        color: #2E86C1;
        text-align: center;
        margin-bottom: 40px;
    }
    .subheader {
        font-size: 30px;
        color: #2874A6;
        margin-bottom: 20px;
    }
    .stButton button {
        background-color: #2874A6;
        color: white;
        font-size: 20px;
        padding: 15px 30px;
    }
    .stNumberInput, .stSelectbox {
        font-size: 20px;
    }
    .emoji {
        font-size: 40px;
        text-align: center;
        display: block;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título de la aplicación
st.markdown('<div class="title">🚗 Predicción de Servicio de Vehículo</div>', unsafe_allow_html=True)

# Emoji destacado
st.markdown('<span class="emoji">🔍</span>', unsafe_allow_html=True)

# Campos de entrada
st.markdown('<div class="subheader">Ingrese los datos del vehículo</div>', unsafe_allow_html=True)

clase = st.selectbox(
    "Clase del vehículo",
    ["Automóvil", "Camioneta", "Motocicleta", "Bus", "Volqueta", "Tractocamión"],
    key="clase",
)

cantidad = st.number_input(
    "Cantidad de vehículos",
    min_value=1,
    step=1,
    format="%d",
    key="cantidad",
)

# Botón de predicción grande y visible
if st.button("🚀 Realizar Predicción", key="predict_button"):
    # Preparar los datos para la predicción
    payload = {
        "input": [
            {
                "clase": clase,
                "cantidad": cantidad
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {DATAROBOT_API_KEY}"
    }

    # Enviar la solicitud a DataRobot
    response = requests.post(PREDICTION_ENDPOINT, json=payload, headers=headers)

    if response.status_code == 200:
        prediction = response.json()
        servicio_predicho = prediction['data'][0]['prediction']
        st.success(f"🏆 Servicio Predicho: {servicio_predicho}", icon="✅")
    else:
        st.error(f"⚠️ Error en la predicción: {response.status_code} - {response.text}", icon="🚫")

# Nota: Asegúrate de configurar tus secretos en Streamlit Cloud
# con los campos: DATAROBOT_API_KEY, DATAROBOT_DEPLOYMENT_ID, DATAROBOT_HOST
