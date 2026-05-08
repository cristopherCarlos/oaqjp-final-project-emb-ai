import requests

def emotion_detector(text_to_analyze):
    # URL del servicio de Detección de Emociones
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Encabezados requeridos por la API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Diccionario con el texto a analizar
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Enviar solicitud POST a la API
    response = requests.post(url, json=myobj, headers=header)
    
    # Retornar el atributo text de la respuesta
    return response.text