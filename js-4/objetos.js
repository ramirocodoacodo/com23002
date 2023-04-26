var persona = {
    nombre: "Juan",
    apellido: "Perez",
    dni: 1234,
    datosPersona: function() {
        return this.nombre + " " + this.apellido;
    },
    datos() {
        return this.nombre + " " + this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona);
console.log(persona.toString());
texto = "Hola Mundo!"
console.log(texto.toString());
console.log(persona.datosPersona());
console.log(persona.datos());

class Perro {
    constructor(nombre, edad) {
        this.nombre = nombre
        this.edad = edad
    }
}

var perro1 = new Perro("Popei", 14);
var perro2 = new Perro("Popei", 14);
perro1.nombre = "Feli";
perro2['edad'] = 16;
console.log(perro1.nombre);
console.log(perro2.nombre);

// string
var texto1 = "Hola Mundo!";
var texto2 = new String("Ramiro");
// texto1 = "Hola";

// prop
console.log(texto2.length);

// métodos
console.log(texto1.charAt(0));
console.log(texto1[0]);
console.log(texto1.replace('Hola', "HOLA"));
console.log(texto1);
console.log(texto1.split(" "));

// document
document.write("Hola Mundo!<br>");
document.write(texto1.toUpperCase() + "<br>");
document.write(texto1.substring(1,3));
