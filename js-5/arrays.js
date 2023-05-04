const nombres = ["Ramiro", "Juan", "Laura"];
let a1 = new Array(1,2,true,[1,1,12,33], "Hola Mundo!");
var numeros = [1,2,3,50,0,-3];
console.log(nombres);
console.log(numeros);

nombres.push("Sofía");
console.log(nombres);
console.log(a1[3]);
listNumeros = a1[3];
console.log(listNumeros[0]);

// Métodos
console.log(numeros.length);
numeros.push(1000, 1001);
console.log(numeros.length);

const fruits = ["Banana", "Orange", "Apple", "Mango"];
nueva_lista = fruits.slice(1,3);

// Insertar
fruits.splice(1,0,"Pera");
console.log(fruits);
// Eliminar
fruits.splice(0,1);
console.log(fruits);
fruits.pop();

console.log(a1[a1.length-1][0]);

console.clear();
delete fruits[0];
console.log(fruits);  // [empty, 'Orange', 'Apple']

console.log(numeros);
// [1, 2, 3, 50, 0, -3, 1000, 1001]
for (let i = 0; i < numeros.length; i++) {
    let element = numeros[i];
    // element *= 2;
    numeros[i] *= 2;
    // console.log(element);
}
console.log(numeros);

persona = {
    nombre: "Ramiro",
    apellido: "Escalante Leiva"
}

for (const key in persona) {
    console.log(key);
}
console.log(numeros);

texto = "Hola Mundo!"
for (const valor of texto) {
    console.log(valor);
}

listaValores = new Array(numeros.values());
console.log(numeros.values());

fruits.sort();
console.log(fruits);

numeros.sort(function(a,b){return b-a});
console.log(numeros);

function mult(elem, i, arr){
    arr[i] = elem*10;
}

numeros.forEach(mult);
console.log(numeros);

nuevoNumeros = numeros.map((num)=>num*10);
console.log(nuevoNumeros);

function esMayor(e){
    return e >=18;
}

// Detecto menores de edad en el evento
edades = [17,18,20];
console.log(edades.every(esMayor));

// localStorage.setItem("nombre", "Ramiro");
nom = localStorage.getItem("nombre");
// document.write(nom);
// sessionStorage.setItem("dato", "asfdfdsfsd");
document.getElementById("miDiv").innerText = nom;
