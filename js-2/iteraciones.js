// while: mientras
// Ciclo exacto
cont = 0;
while (cont < 5) {
    cont++;  // cont = cont + 1;
    console.log(cont);
}

// Ciclo Condicional
var num = parseInt(prompt("Ingrese un num:"))
suma = 0;
while (num != 0){
    suma += num;  // suma = suma + num;
    num = parseInt(prompt("Ingrese un num:"))
}
console.log(suma)

console.clear();

// do-while
var menu;
do {
    menu = parseInt(prompt("Ingrese una opción:"));
// } while (!(menu >= 1 && menu <= 5));
} while (menu < 1 || menu > 5);
console.log(menu);

// break;

// for
for (let i=1; i<=5; i++){
    console.log(i);
    if (i==3)
        break;  // Mala práctica
}
