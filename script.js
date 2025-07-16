function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (message === "") return;

    const chatBox = document.getElementById("chatBox");
    chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;

    fetch("https://ai-based-chatbot-with-web-interface.onrender.com/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        chatBox.innerHTML += `<p><strong>Bot:</strong> Sorry, something went wrong.</p>`;
        console.error("Error:", error);
    });

    input.value = "";
}
