function sumar(num1, num2) {
    let suma = num1 + num2;
    return suma;
    console.log(suma);
}

// parámetro por defecto
function sumar3(num1, num2, num=0) {
    let suma = num1 + num2 + num;
    return suma;
    console.log(suma);
}

var mostrar = function (texto) {
    console.log(texto);
} 

// resultado = sumar(10,2);
resultado = sumar3(10,2,5);
console.log(resultado);
console.log(sumar); /* ƒ sumar(num1, num2) {
    let suma = num1 + num2;
    return suma;
    console.log(suma);
}*/

// let vs. var
var a = 5;
function procesar(){
    if (true) {
        
        let b = 2 + a;
    }
    return b;
}
console.log(a);
// console.log(b);

// funciones flecha
var sumar = (num1, num2) => num1 + num2;

// num3 = 1000;
// función anónima
var sumar = function (num1, num2) {
    return num1 + num2;
}

c = 100;
console.clear();
mostrar(sumar(c,5));
mostrar(sumar);

console.clear();

// callbacks
function procesarEntrada(callback) {
    let nombre = prompt("Ingrese su nombre:");
    callback(nombre);
}

procesarEntrada(mostrar);

// clousures
function crearFuncion(valorASumar) {
    return function(num) {
        return num + valorASumar;
    }
}

let sumarX = crearFuncion(5);
const sumar10 = crearFuncion(10);
mostrar(sumarX);
mostrar(sumar10);
/*
ƒ (num) {
        return num + valorASumar;
    }
*/

mostrar(sumarX(10));
mostrar(sumar10(10));
