class NumeroNegativoError(Exception):
    pass

num = int(input("Ingrese un número positivo: "))
if num <= 0:
    raise NumeroNegativoError("El número no pueder ser cero.")

print(num)
