import requests
import pyttsx3
import constantes

def call_gemini(text):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": text}]
            }
        ]
    }
    try:
        response = requests.post(constantes.GEMINI_URL, json=payload, headers=headers, timeout=60)
        print("# Respuesta API:", response.text)
        response.raise_for_status()  # manejo de errores HTTP
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print("# Errore HTTP:", errh)
        return {"error": f"Errore HTTP: {errh}"}
    except requests.exceptions.ConnectionError as errc:
        print("# Error de conexión:", errc)
        return {"error": f"Error de conexión: {errc}"}
    except requests.exceptions.Timeout as errt:
        print("# Timeout:", errt)
        return {"error": f"Timeout: {errt}"}
    except requests.exceptions.RequestException as err:
        print("# Error genérico:", err)
        return {"error": f"Error genérico: {err}"}

def call_llmstudio(text):
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.2-3b-instruct",
        "messages": [
            {"role": "system", "content": "Contesta en español, de manera clara y precisa."},
            {"role": "user", "content": text}
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }

    try:
        response = requests.post(constantes.LLMSTUDIO_URL, json=payload, headers=headers, timeout=10)
        response.raise_for_status()  # manejo errores HTTP
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as errh:
        print("# Error HTTP:", errh)
        return "Error HTTP en la petición a LLM Studio."
    except requests.exceptions.ConnectionError as errc:
        print("# Error de conexión:", errc)
        return "Error de conexión: asegurate de que LLM Studio esté activo."
    except requests.exceptions.Timeout as errt:
        print("# Timeout:", errt)
        return "Timeout en la petición a LLM Studio."
    except requests.exceptions.RequestException as err:
        print("# Error general:", err)
        return "Error general en la petición a LLM Studio."

# reproducir voz
def text_to_speech(text):
    engine = pyttsx3.init()
    # muestro las voces que mi ordenador tiene disponibles y escojo el id en español
    # for voz in engine.getProperty('voices'):
    #     print(voz)
    engine.setProperty('voice', constantes.VOZ_ES)
    engine.say(text)
    engine.runAndWait()

# extraer el formato JSON
def extract_text_mkarkdown(respuesta_json):
    try:
        return respuesta_json["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("# Error al extarer Markdown:", e)
        return ""
    

