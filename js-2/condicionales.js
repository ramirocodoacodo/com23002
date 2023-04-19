
// console.clear()
console.log("Estructuras condicionales");
var num = parseInt(prompt("Ingrese un número:"));
// Condicional simple
if (!(num > 0)) {
    // Indentación
    alert("El número es negativo o cero.");
}

// Condicional doble
if (num > 0) {
    // Indentación
    alert("El número es positivo.");
} 
else {
    alert("El número es negativo o cero.");
}

// Condicional anidado
if (num > 0)
    alert("El núm es +.")
else
    if (num < 0)
        alert("El múm. es -.")
    else
        alert("El núm. es cero.")

// else if: elif (NO existe en JS)
if (num > 0)
    alert("El núm es +.")
else if (num < 0)
    alert("El múm. es -.")
else
    alert("El núm. es cero.")

// switch
var menu = parseInt(prompt("Ingrese una opción:"));
switch (menu) {
    case 1:
        console.log("Opción 1: alta de usuario");
        break;
    case 2:
    case 3:
        console.log("Opción 2: baja de usuario");
        break;
    default:
        console.log("Ha seleccionado una opción no válida.")
}

// Operador ternario
var num = -2;
resultado = num > 0 ? "Positivo" : "Negativo o cero."
console.log(num > 0 ? "Positivo" : "Negativo o cero.")
console.log(resultado);
