from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import lib
from obtener_contexto import get_plugin_context

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# endpoint envio texto GEMINI 
@app.route('/send_text', methods=['POST'])
def send_text():
    text = request.json.get("text", "")
    if not text.strip():
        return jsonify({"error": "El campo de texto está vacío."})

    context = get_plugin_context(text)
    if not context.strip():
        context = "No se encontró documentación relevante para esta consulta."

    prompt_rag = f"""
Eres un experto en plugins de Moodle. A continuación, se proporciona documentación relacionada. Responde a la pregunta del usuario de forma clara y precisa en español.

=== DOCUMENTACIÓN ===
{context}

=== PREGUNTA ===
{text}

=== RESPUESTA ===
"""
    response = lib.call_gemini(prompt_rag)

    if isinstance(response, dict) and "candidates" in response:
        response_text = response["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"response": response_text})

    return jsonify({"error": "Formato de respuesta desconocido", "raw": response})


# endpoint envio voz LLM Studio
@app.route('/send_voice', methods=['POST'])
def send_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 0.85 # tiempo de espera antes de cerrar
        print("# Escuchando...")
        audio = recognizer.listen(source, phrase_time_limit=10)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        print(f"# Texto reconocido: {text}")

        if not text.strip():
            return jsonify({"error": "El campo de texto está vacío."})
        context = get_plugin_context(text)
        if not context.strip():
            context = "No se encontró documentación relevante para esta consulta."

        context = get_plugin_context(text)
        prompt_rag = f"""
Eres un experto en plugins de Moodle. A continuación, se proporciona documentación relacionada. Responde a la pregunta del usuario de forma clara y precisa en español.

=== DOCUMENTACIÓN ===
{context}

=== PREGUNTA ===
{text}

=== RESPUESTA ===
"""
        response = lib.call_llmstudio(prompt_rag)

        print(f"# Respuesta desde LLM Studio: {response}")

        # convertir texto en audio
        lib.text_to_speech(response)

        return jsonify({
            "response": response,
            "transcript": text
        })
    except sr.UnknownValueError:
        return jsonify({"error": "No he entendido"})
    except sr.RequestError:
        return jsonify({"error": "Error de conexión a LLM Studio"})
    except:
        return jsonify({"error": "Error inesperado"})

if __name__ == '__main__':
    app.run(debug=True)
