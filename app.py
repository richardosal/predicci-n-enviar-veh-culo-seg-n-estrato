import streamlit as st
import requests

# Configuración de la API de DataRobot
DATAROBOT_API_KEY = st.secrets["DATAROBOT_API_KEY"]
DATAROBOT_DEPLOYMENT_ID = st.secrets["DATAROBOT_DEPLOYMENT_ID"]
DATAROBOT_HOST = st.secrets["DATAROBOT_HOST"]  # Por ejemplo, "https://app.datarobot.com"
PREDICTION_ENDPOINT = f"{DATAROBOT_HOST}/api/v2/deployments/{DATAROBOT_DEPLOYMENT_ID}/predictions"

# Título de la aplicación
st.title("🚗 Predicción de Servicio de Vehículo")

# Campos de entrada
st.subheader("Ingrese los datos del vehículo")

clase = st.selectbox(
    "Clase del vehículo",
    ["Automóvil", "Camioneta", "Motocicleta", "Bus", "Volqueta", "Tractocamión"]
)

cantidad = st.number_input(
    "Cantidad de vehículos",
    min_value=1,
    step=1,
    format="%d"
)

# Botón de predicción
if st.button("Realizar Predicción", key="predict_button"):
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
        st.success(f"Servicio Predicho: {servicio_predicho}")
    else:
        st.error(f"Error en la predicción: {response.status_code} - {response.text}")

# Nota: Asegúrate de configurar tus secretos en Streamlit Cloud
# con los campos: DATAROBOT_API_KEY, DATAROBOT_DEPLOYMENT_ID, DATAROBOT_HOST
