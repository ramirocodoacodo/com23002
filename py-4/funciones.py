def sumar(num1, num2, num3=0):
    # docstring
    '''
    pre: recibe 2 números.
    pos: devuelve la suma de ambos números.

    '''
    resultado = num1 + num2 + num3  # Var. Global
    return resultado  # Buena práctica: un sólo return al final

# Prog ppal
# help(sumar)

num = int(input("Ingrese un número: "))
print(sumar(1,3))
print(sumar(1,3,num3=10))
print(sumar(num3=10,num1=1,num2=3))

print("Hola", end=' ')
print("Mundo!")
