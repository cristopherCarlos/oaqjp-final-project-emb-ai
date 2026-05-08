"""
Servidor Flask para la aplicación de Detección de Emociones.
Este módulo define las rutas para procesar el análisis de emociones
y renderizar la interfaz de usuario.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Recibe el texto del usuario desde la interfaz web, lo envía al 
    analizador de emociones y devuelve el resultado formateado.
    """
    # Obtener el texto de los argumentos de la solicitud
    text_to_analyze = request.args.get('textToAnalyze')

    # Obtener la respuesta del detector de emociones
    response = emotion_detector(text_to_analyze)

    # Extraer las puntuaciones y la emoción dominante
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Validar si la entrada fue exitosa
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página de inicio (index.html).
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)