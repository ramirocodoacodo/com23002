from Mascota import Mascota

class Veterinaria:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.__mascotas = []

    def agregar_mascota(self, m):
        self.__mascotas.append(m)

    def __str__(self):
        cadena = ''
        cadena += f'Nombre: {self.nombre}\n'
        cadena += 'Listado de mascotas de la Vete:' + '\n'
        for m in self.__macostas:
            cadena += str(m) + '\n'
        cadena += '\n'
        return cadena

# Prog ppal
'''
v1 = Veterinaria('Vete Codo')
m1 = Mascota('Firulais', 'M')
print(m1)
# m1.nombre = 'sada'  # AttributeError: can't set attribute
m1.__nombre = 'sada'  # No modifico el atributo privado
m1.raza = 'Mestizo'
m1.cumplir_anios()
print(m1)

'''