from Mascota import Mascota
from Mascota import Duenio

class Perro(Mascota):
    def __init__(self, nombre, raza):
        super().__init__(nombre, raza)
        self.__especie = 'Perro'

    def emitir_sonido(self):
        return 'Guau'

    # Sobreeescrimo el método str
    def __str__(self):
        cadena = super().__str__()
        return cadena + ', Especie: ' + self.__especie

def __main__():
    p1 = Perro('Paka', 'Mestiza')
    print(p1)
    print(p1.emitir_sonido())

if __name__ == '__main__':
    __main__()