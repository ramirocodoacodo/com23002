// Operadores de asignación
cont = 0;
cont += 1;  // cont = cont + 1;
cont -= 1;  // cont = cont - 1;

num = 1;
console.log(num);
num *= 2;  // num = num * 2;
console.log(num);
num *= 2;
console.log(num);
num *= 2;
console.log(num);
num *= 2;
console.log(num);
num *= 2;
console.log(num);

// operadores relacionales (comparación)
// var A = "2";
var A = 5;
// B = 2.0;
B = 2;
console.log(A == B);  // true
console.log(A === B);  // false
console.log(A != B);  // false
console.log(A >= B);  // true

// Operadores lógicos
// AND: &&
// OR: || pipe
// NOT: !
console.clear();
console.log(A >= 5-2*2 && B == 0);  // true && false => false
console.log(true && false && true);
console.log(true || false);

// op. incrementales
// op. ternario

// Operadores de cadena
texto1 = "Ramiro";
texto2 = "Escalante Leiva";
texto3 = texto1 + " " + texto2;
console.log(texto3);  // Ramiro Escalante Leiva

texto = "";
textoVar = "Ramiro";
texto += textoVar;  // texto = texto + textoVar
textoVar = " ";
texto += textoVar;  // texto = texto + textoVar
textoVar = "Escalante Leiva";
texto += textoVar;  // texto = texto + textoVar
console.log(texto)
