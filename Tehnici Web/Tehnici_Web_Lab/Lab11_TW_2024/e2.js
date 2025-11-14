window.onload = function () {

    let canvas = document.getElementById('canvas');
    let ctx = canvas.getContext("2d");
    let colors = ["red", "green", "blue", "yellow", "purple", "lime"];

    function drawCircle(x, y, r, color) {
        ctx.beginPath();
        ctx.arc(x, y, r, 0, 2 * Math.PI);
        ctx.fillStyle = color;
        ctx.fill();
        ctx.closePath();
    }
    //drawCircle(500, 100, 50, "lime");
    function drawLights() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < 15; i++) {
            let r = 20;
            let x = 45 + i * 65;
            let y = canvas.height / 2;
            let rx = Math.floor(Math.random() * canvas.width);
            let ry = Math.floor(Math.random() * canvas.height);
            let color = colors[Math.floor(Math.random() * colors.length)];
            console.log(color);
            drawCircle(rx, ry, r, color);
        }
    }
    function animatie() {
        setInterval(drawLights, 500);

    }
    animatie()
}