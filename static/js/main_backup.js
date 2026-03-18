async function sendMessage() {
    let input = document.getElementById("user-input");
    let msg = input.value;
    if (!msg) return;

    let messages = document.getElementById("messages");

    // Show user message
    messages.innerHTML += `<div class="user">USER > ${msg}</div>`;
    input.value = "";

    // Send to Flask
    let res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    });

    let data = await res.json();

    // Jarvis typing effect
    let jarvisDiv = document.createElement("div");
    jarvisDiv.className = "jarvis";
    jarvisDiv.innerHTML = "JARVIS > ";
    messages.appendChild(jarvisDiv);

    typeWriter(jarvisDiv, data.answer);

    // Show sources
    if (data.answer) {
        messages.innerHTML += `<div class="system"></div>`;
        messages.innerHTML = `<div class="system">${data.answer}</div>`
        //I need prompt user to show the knowlwdge sources if user wishes
    }

    messages.scrollTop = messages.scrollHeight;
}

// TYPEWRITER EFFECT
function typeWriter(element, text) {
    let i = 0;
    let cursor = document.createElement("span");
    cursor.className = "cursor";
    cursor.innerHTML = " ";
    element.appendChild(cursor);

    let interval = setInterval(() => {
        element.innerHTML = element.innerHTML.replace(cursor.outerHTML, "");
        element.innerHTML += text[i] + cursor.outerHTML;
        i++;

        if (i >= text.length) {
            clearInterval(interval);
        }
    }, 20);
}
