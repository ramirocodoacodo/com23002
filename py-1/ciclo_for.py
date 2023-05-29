# for
# for i in range(10):  # 0 .. 9
# for i in range(1,11):  # 1 .. 10
for i in range(1,11,2):  # 1 .. 9
    print(i, end=" ")
print()  # Salto de línea

# operador in con cadenas
cadena = "Ramiro"
print("R" in cadena)  # True
print("e" not in cadena)  # True

# listas y for
numeros = [1,2,3,0,-1,100]
for valor in numeros:
    print(valor, end=" ")
print()

for i in range(len(numeros)):
    print(str(i) + ":", numeros[i])
print()
