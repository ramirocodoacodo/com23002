import random

def mostrar_lista(lista):
    ''' Muestra el contenido de una lista.
    '''
    for valor in lista:
        print(valor, end= ' ')
    print()  # salto de línea

numeros = [1,2,3,100,-10]
mostrar_lista(numeros)
print(mostrar_lista(numeros))  # None

def duplicar(lista):
    # for valor in lista:
    #     valor *= 2  # valor = valor * 2
    #     print(valor)
    for i in range(len(lista)):  # 0..4
        lista[i] *= 2

print(numeros)
duplicar(numeros)
print(numeros)

# listas, diccionarios (mutables) vs cadenas, tuplas (no mutables)
nombre = "Ramiro"
print(nombre*2)
# nombre[0] = "r"  # TypeError: 'str' object does not support item assignment

nombre = nombre*2
print(nombre)

# tuplas
def calcular_suma_prom(lista):
    suma = sum(lista)
    n = len(lista)
    prom = suma / n

    return suma, prom  # Tupla: (192, 38.4)

print(calcular_suma_prom(numeros))
sumatoria, promedio = calcular_suma_prom(numeros)  # Desempaquetar

# import
def crear_lista(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(1,10))

    return lista

# print(lista)  # NameError: name 'lista' is not defined
numeros2 = crear_lista(10)
mostrar_lista(numeros2)

# lambda / anónimas / callback
def fx_cuadrado(num):
    return num**2

cuadrado = lambda num:num**2

print(fx_cuadrado(2))
print(cuadrado(2))
# help(cuadrado)

print(numeros2)
# cuadrados = list(map(cuadrado, numeros2))
cuadrados = list(map(lambda num:num**2, numeros2))
print(cuadrados)
