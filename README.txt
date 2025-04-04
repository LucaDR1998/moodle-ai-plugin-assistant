# Moodle AI Plugin Assistant

This project implements a full-stack AI-powered web application that allows Moodle administrators to intelligently query plugin documentation. It combines **generative AI** (Gemini / LLM Studio), **vector search** (Milvus), and **automatic documentation generation**.

---

## Technologies Used

- **Python (Flask)** – backend API
- **Bootstrap + JavaScript (AJAX)** – frontend UI
- **Gemini API (Google)** – for text-based LLM responses
- **LLM Studio (local)** – for voice command responses
- **Milvus (Zilliz Cloud)** – vector database for plugin documentation
- **SentenceTransformers** – embedding generation
- **SpeechRecognition + pyttsx3** – voice input/output

---

## Full System Flow

### 1. Documentation Generation

**File:** `generate_documentation.py`  
Generates `.md` documents for each Moodle plugin using Gemini API (description, install guide, FAQ, common issues).

Output: stored in `docs_plugins/`

---

### 2. Indexing Markdown into Milvus

**File:** `indexar_documentacion.py`  
Splits `.md` files, embeds them with MiniLM-L6-v2, and uploads to Milvus.

- Creates semantic index (Cosine + IVF_FLAT)
- Stores: plugin name, fragment, vector

---

### 3. Flask API with AI Endpoints

**File:** `flask_API.py`

Endpoints:

- `POST /send_text`: text input → search Milvus → Gemini → response
- `POST /send_voice`: record voice → transcribe → search Milvus → LLM Studio → response + TTS

The system uses **RAG (Retrieval Augmented Generation)** to improve precision by injecting context into the prompt before calling the AI.

---

### 4. Web Interface

**Frontend files:**

- `templates/index.html`
- `static/chat.js`

Features:

- Chat box for text
- Mic button for voice
- Real-time AJAX communication
- Response rendering and TTS output

---

## RAG Flow: Retrieval-Augmented Generation

1. Convert query to embedding
2. Search similar fragments in Milvus
3. Inject context into LLM prompt
4. Get a response from Gemini / LLM Studio
5. Display + optionally speak the answer

---

## Run Instructions (coming soon)

> To be added: virtual environment setup, `.env` config, and how to start the API.

---

## Author

**Luca Demicheli Rubio**  
Email: [lucademichelirubio.portfolio@gmail.com](mailto:lucademichelirubio.portfolio@gmail.com)  
Portfolio: [https://luca-demicheli-rubio.com](https://luca-demicheli-rubio.com)

---

## License

MIT
