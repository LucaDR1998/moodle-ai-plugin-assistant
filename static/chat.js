document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('textInput');
    const sendText = document.getElementById('sendText');
    const sendVoice = document.getElementById('sendVoice');
    const output = document.getElementById('output');

    function appendMessage(text, sender = "ai") {
        const div = document.createElement("div");
        div.className = sender === "user" ? "user-message" : "ai-message";
        div.innerHTML = text;
        output.appendChild(div);
        output.scrollTop = output.scrollHeight;
    }

    sendText.addEventListener('click', () => {
        const userMessage = textInput.value.trim();
        if (userMessage === '') return;

        appendMessage(userMessage, "user");

        fetch("/send_text", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: userMessage })
        })
            .then(response => response.json())
            .then(data => {
                if (data.response) {
                    appendMessage("<strong>Gemini:</strong> " + data.response, "ai");
                } else if (data.error) {
                    appendMessage("# Error: " + data.error, "ai");
                } else {
                    appendMessage("# Respuesta desconocida", "ai");
                }
            })
            .catch(err => {
                console.error("Error:", err);
                appendMessage("# Error de red", "ai");
            });

        textInput.value = '';
    });

    sendVoice.addEventListener('click', () => {
        appendMessage("Estoy escuhando...", "user");

        fetch("/send_voice", { method: "POST" })
            .then(response => response.json())
            .then(data => {
                if (data.response && data.transcript) {
                    appendMessage(data.transcript, "user");
                    appendMessage("<strong>LLM Studio:</strong> " + data.response, "ai");
                } else if (data.response) {
                    appendMessage("<strong>LLM Studio:</strong> " + data.response, "ai");
                } else if (data.error) {
                    appendMessage("# Error: " + data.error, "ai");
                } else {
                    appendMessage("# Respuesta desconocida", "ai");
                }
            })
            .catch(err => {
                console.error("Error:", err);
                appendMessage("# Error petición vocal", "ai");
            });
    });
});
