# Categorizar calificaciones de estudiantes (1 a 10)
# nota = int(input("Ingrese una nota: "))
# Condicionales
'''
if nota >= 7:
    print("PROMOCIONA")  # Indentación
else:
    if nota >= 4 and nota < 7:
        print("APRUEBA")
    else:
        if 1 <= nota < 4:
            print("DESAPRUEBA")
        else:
            print("Nota no válida.")
'''
# elif
'''
if nota >= 7 and nota <= 10:
    print("PROMOCIONA")  # Indentación
elif nota >= 4 and nota < 7:
    print("APRUEBA")
elif 1 <= nota < 4:
    print("DESAPRUEBA")
else:
    print("Nota no válida.")
'''

# switch (desde la versión 3.11)

# Ingresar calificaciones de estudiantes y calcular un promedio (hasta ingreso 0)
# bucles: while
suma = 0
cont = 0
# Validación
nota = int(input("Ingrese una nota: "))
while not(nota >= 0 and nota <= 10):
    print("Nota no válida.")
    nota = int(input("Error. Ingrese una nota: "))

while nota != 0:
    suma = suma + nota
    cont += 1  # cont = cont + 1
    if nota >= 7 and nota <= 10:
        print("PROMOCIONA")  # Indentación
    elif nota >= 4 and nota < 7:
        print("APRUEBA")
    else:
        print("DESAPRUEBA.")
    nota = int(input("Ingrese una nota: "))
    while not(nota >= 0 and nota <= 10):
        print("Nota no válida.")
        nota = int(input("Error. Ingrese una nota: "))

if cont != 0:
    promedio = suma / cont
    print("El promedio es:", promedio)  # ZeroDivisionError: division by zero
else:
    print("No ha ingresado valores.")
print("fin del programa.")

