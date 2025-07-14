function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (message === "") return;

    const chatBox = document.getElementById("chatBox");
    chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;

    fetch("chatbot_runner.php", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "message=" + encodeURIComponent(message)
    })
    .then(response => response.text())
    .then(reply => {
        chatBox.innerHTML += `<p><strong>Bot:</strong> ${reply}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    input.value = "";
}
