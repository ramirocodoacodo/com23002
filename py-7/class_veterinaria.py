from Mascota import Mascota
from Perro import Perro
from Gato import Gato
from Pajaro import Pajaro

class Veterinaria:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.__mascotas = []

    def agregar_mascota(self, m):
        self.__mascotas.append(m)

    def despertar_mascotas(self):
        for mascota in self.__mascotas:
            print(mascota.emitir_sonido())

    def __str__(self):
        cadena = ''
        cadena += f'Nombre: {self.nombre}\n'
        cadena += 'Listado de mascotas de la Vete:' + '\n'
        for m in self.__macostas:
            cadena += str(m) + '\n'
        cadena += '\n'
        return cadena

# Prog ppal
def __main__():
    v1 = Veterinaria('Vete Codo')
    m1 = Perro('Firulais', 'M')
    m2 = Gato('Neko','M')
    m3 = Pajaro('Piolin','Canario')
    v1.agregar_mascota(m1)
    v1.agregar_mascota(m2)
    v1.agregar_mascota(m3)
    print(m1)
    # m1.nombre = 'sada'  # AttributeError: can't set attribute
    m1.__nombre = 'sada'  # No modifico el atributo privado
    m1.raza = 'Mestizo'
    m1.cumplir_anios()
    print(m1)
    v1.despertar_mascotas()

if __name__ == '__main__':
    __main__()