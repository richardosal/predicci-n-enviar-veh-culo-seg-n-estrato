import streamlit as st
import requests
import json

# Configura tus credenciales y endpoint
DATAROBOT_API_KEY = "TU_API_KEY"
DATAROBOT_DEPLOYMENT_ID = "TU_DEPLOYMENT_ID"
DATAROBOT_HOST = "https://app.datarobot.com"
PREDICTION_ENDPOINT = "URL_DEL_ENDPOINT_DE_PREDICCIÓN"

# Título de la app
st.title("Predicción de Servicio Vehicular 🚗")

# Ingreso de variables
clase = st.selectbox("Selecciona la clase del vehículo", 
                     ["Automóvil", "Camioneta", "Motocicleta", "Bus", "Volqueta", "Tractocamión"])

cantidad = st.number_input("Cantidad registrada", min_value=0, step=1)

# Botón para enviar
if st.button("Predecir Servicio"):
    # Construimos la entrada para la API
    payload = {
        "input_data": [
            {
                "clase": clase,
                "cantidad": cantidad
            }
        ]
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {DATAROBOT_API_KEY}'
    }

    # Hacemos la petición a DataRobot
    response = requests.post(PREDICTION_ENDPOINT, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        result = response.json()
        # Suponiendo que la predicción está en result['prediction']
        prediccion = result['prediction'][0]['prediction']
        st.success(f"Servicio Predicho: {prediccion}")
    else:
        st.error(f"Error en la predicción: {response.status_code} - {response.text}")
