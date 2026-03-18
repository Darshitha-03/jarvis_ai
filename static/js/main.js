async function sendMessage() {
    let input = document.getElementById("user-input");
    let msg = input.value;
    if (!msg) return;

    let messages = document.getElementById("messages");

    // Show user message
    let userDiv = document.createElement("div");
    userDiv.className = "user";
    userDiv.innerText = "USER > " + msg;
    messages.appendChild(userDiv);

    input.value = "";

    // Send to Flask
    let res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    });

    let data = await res.json();
    console.log("DEBUG RESPONSE:", data);

    // Create Jarvis message container
    let jarvisDiv = document.createElement("div");
    jarvisDiv.className = "jarvis";
    jarvisDiv.innerText = "JARVIS > ";
    messages.appendChild(jarvisDiv);

    let answer = data.answer || "No response received";

    // ✅ SIMPLE render (NO typewriter for now)
    jarvisDiv.innerText = "JARVIS > " + answer;

    messages.scrollTop = messages.scrollHeight;
}