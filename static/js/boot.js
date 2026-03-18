const bootLines = [
    "JARVIS loading..."
];

let index = 0;
let bootText = document.getElementById("boot-text");

function showLine(line) {
    bootText.style.opacity = 0;
    setTimeout(() => {
        bootText.innerHTML = line;
        bootText.style.opacity = 1;
    }, 300);
}

function bootSequence() {
    if (index < bootLines.length) {
        showLine(bootLines[index]);
        index++;
        setTimeout(bootSequence, 2000);
    } else {
        // Fade out boot text
        setTimeout(() => {
            bootText.style.opacity = 0;

            // Fade HUD rings
            document.getElementById("hud").style.opacity = 0;

            // Show main UI
            document.getElementById("main-ui").style.display = "block";

            // Completely remove boot text after fade
            setTimeout(() => {
                bootText.style.display = "none";
            }, 1500);

        }, 1000);
    }
}

bootSequence();
