from Mascota import Mascota
from Mascota import Duenio

class Pajaro(Mascota):
    def __init__(self, nombre, raza):
        super().__init__(nombre, raza)
        self.__especie = 'Perro'

    def emitir_sonido(self):
        return 'Pio pio'

    # Sobreeescrimo el método str
    def __str__(self):
        cadena = super().__str__()
        return cadena + ', Especie: ' + self.__especie
