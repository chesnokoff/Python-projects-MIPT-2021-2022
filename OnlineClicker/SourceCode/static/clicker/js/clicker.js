var add_value = 0;

setInterval(function () {
    document.getElementById("score").innerHTML =
        String(Number(document.getElementById("score").innerHTML) + add_value);
}, 1500);

function Buy(cost, power) {
    let score = Number(document.getElementById("score").innerHTML)
    if (score < cost) {
        return
    }
    document.getElementById("score").innerHTML = String(Number(
        document.getElementById("score").innerHTML) - cost);
    add_value = add_value + power
}

function Click() {
    document.getElementById("score").innerHTML = String(Number(
        document.getElementById("score").innerHTML) + 1);
}