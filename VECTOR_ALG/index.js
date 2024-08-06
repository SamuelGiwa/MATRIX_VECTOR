const canvas = document.getElementById('vectorCanvas');
const ctx = canvas.getContext('2d');

function drawVector(x, y, color) {
    const startX = 300;
    const startY = 200;
    const endX = startX + x * 50;
    const endY = startY - y * 50;
    const headLength = 10; 
    const angle = Math.atan2(endY - startY, endX - startX);

    ctx.beginPath();
    ctx.moveTo(startX, startY);
    ctx.lineTo(endX, endY);
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.closePath();

    ctx.beginPath();
    ctx.moveTo(endX, endY);
    ctx.lineTo(endX - headLength * Math.cos(angle - Math.PI / 6), endY - headLength * Math.sin(angle - Math.PI / 6));
    ctx.moveTo(endX, endY);
    ctx.lineTo(endX - headLength * Math.cos(angle + Math.PI / 6), endY - headLength * Math.sin(angle + Math.PI / 6));
    ctx.stroke();
    ctx.closePath();
}

function drawVectors() {
    const vec1x = parseFloat(document.getElementById('vec1x').value);
    const vec1y = parseFloat(document.getElementById('vec1y').value);
    const vec2x = parseFloat(document.getElementById('vec2x').value);
    const vec2y = parseFloat(document.getElementById('vec2y').value);

   
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawVector(vec1x, vec1y, 'red');
    drawVector(vec2x, vec2y, 'blue');

    const resultantX = vec1x + vec2x;
    const resultantY = vec1y + vec2y;
    drawVector(resultantX, resultantY, 'green');
}