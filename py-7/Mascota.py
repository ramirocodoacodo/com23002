from abc import ABC, abstractmethod

class Mascota(ABC):
    # nombre = "Vete Codo"
    def __init__(self, nombre, raza):
        # atributo privado
        self.__nombre = nombre
        # self.raza = raza
        self.__raza = raza
        self.__edad = 0

    # Getters y Setters
    # Atributo nombre
    @property  # decorador
    def nombre(self):
        return self.__nombre

    @property  # decorador
    def raza(self):
        return self.__raza
    
    @raza.setter
    def raza(self, raza):
        if raza != '':
            self.__raza = raza

    @property
    def edad(self):
        return self.__edad

    def cumplir_anios(self):
        self.__edad += 1

    @abstractmethod
    def emitir_sonido(self):
        print('El animal emite sonido: ')

    def __str__(self):
        cadena = 'Nombre: ' + self.__nombre + ', Raza: ' + self.raza + ', Edad: ' + str(self.__edad)
        return cadena

class Duenio:
    pass

# Prog. ppal
def __main__():
    m1 = Mascota("Firulais", 'Mestizo')

    print(m1.raza)
    # print(m1.__nombre)  # AttributeError: 'Mascota' object has no attribute '__nombre'
    print(m1.nombre)
    # m1.nombre = 'sdasd'  # AttributeError: can't set attribute
    m1.__nombre = 'sdasd'
    m1.raza = ''
    print(m1)
    m1.cumplir_anios()
    print(m1)

if __name__ == '__main__':
    __main__()

print(__name__)
