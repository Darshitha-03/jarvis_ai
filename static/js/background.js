const canvas = document.getElementById("bg-canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let nodes = [];
let mouse = { x: null, y: null };

// Create floating AI nodes
for (let i = 0; i < 120; i++) {
    nodes.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 2 + 1,
        vx: (Math.random() - 0.5) * 0.2,
        vy: (Math.random() - 0.5) * 0.2
    });
}

// Mouse hover effect
window.addEventListener("mousemove", e => {
    mouse.x = e.x;
    mouse.y = e.y;
});

function drawGrid() {
    ctx.strokeStyle = "rgba(0,255,255,0.08)";
    for (let x = 0; x < canvas.width; x += 80) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();
    }
    for (let y = 0; y < canvas.height; y += 80) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
    }
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawGrid();

    // Floating AI nodes
    nodes.forEach(n => {
        n.x += n.vx;
        n.y += n.vy;

        if (n.x < 0) n.x = canvas.width;
        if (n.x > canvas.width) n.x = 0;
        if (n.y < 0) n.y = canvas.height;
        if (n.y > canvas.height) n.y = 0;

        // Glow node
        ctx.fillStyle = "cyan";
        ctx.shadowBlur = 12;
        ctx.shadowColor = "cyan";
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
        ctx.fill();

        // Hover glow
        if (mouse.x && Math.hypot(n.x - mouse.x, n.y - mouse.y) < 120) {
            ctx.fillStyle = "rgba(255,255,255,0.7)";
            ctx.beginPath();
            ctx.arc(n.x, n.y, n.r + 2, 0, Math.PI * 2);
            ctx.fill();
        }
    });

    requestAnimationFrame(draw);
}

draw();
