const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-btn");

const API_URL = "http://127.0.0.1:8000/chat";

sendButton.addEventListener("click", sendMessage);

userInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
    sendMessage();
    }
});

async function sendMessage() {
    const message = userInput.value.trim();

    if (!message) {
    return;
    }

    addMessage(message, "user-message");
    userInput.value = "";

    sendButton.disabled = true;
    sendButton.textContent = "Thinking...";

    try {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
        "Content-Type": "application/json"
        },
        body: JSON.stringify({
        message: message
        })
    });

    if (!response.ok) {
        throw new Error("Something went wrong with the backend request.");
    }

    const data = await response.json();

    addMessage(data.answer, "bot-message");
    } catch (error) {
    addMessage(
        "Sorry, something went wrong. Make sure your backend is running.",
        "error-message"
    );
    console.error(error);
    } finally {
    sendButton.disabled = false;
    sendButton.textContent = "Send";
    userInput.focus();
    }
}

function addMessage(text, className) {
    const messageElement = document.createElement("div");
    messageElement.className = className;
    messageElement.textContent = text;

    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}