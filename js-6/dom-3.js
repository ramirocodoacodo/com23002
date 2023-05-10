function cambiarFondo() {
    var elem = document.querySelector(".ejemplo");
    elem.style.backgroundColor = "blue";
    // document.querySelector("button").innerHTML = "Gracias!"
    document.querySelector("#mi-boton").innerHTML = "Gracias!"
}

function cambiarTodos() {
    var elementos = document.querySelectorAll(".ejemplo");
    for (let index = 0; index < elementos.length; index++) {
        const element = elementos[index];
        element.style.backgroundColor = "blue";
    }
}
