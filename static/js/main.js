async function sendMessage() {
    let input = document.getElementById("user-input");
    let msg = input.value;
    if (!msg) return;

    let messages = document.getElementById("messages");

    let userDiv = document.createElement("div");
    userDiv.className = "user";
    userDiv.innerText = "USER > " + msg;
    messages.appendChild(userDiv);

    input.value = "";

    let res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    });

    let data = await res.json();

    let jarvisDiv = document.createElement("div");
    jarvisDiv.className = "jarvis";
    jarvisDiv.innerText = "JARVIS > " + data.answer;
    messages.appendChild(jarvisDiv);

    messages.scrollTop = messages.scrollHeight;
}

/* ---------- FILE UPLOAD ---------- */

function openFilePicker() {
    document.getElementById("fileInput").click();
}

document.getElementById("fileInput").addEventListener("change", uploadFile);

async function uploadFile(event) {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    let res = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    let data = await res.json();

    alert(data.message);

    // update UI list
    addFileToList(file.name);
}

/* ---------- FILE LIST UI ---------- */

function addFileToList(filename) {
    const list = document.getElementById("file-list");

    // Remove duplicate if exists
    let existing = document.getElementById("file-" + filename);
    if (existing) {
        existing.remove();
    }

    let li = document.createElement("li");
    li.id = "file-" + filename;
    li.innerText = filename;

    list.appendChild(li);
}