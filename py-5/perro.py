# Definir nuestra clase
class Perro:
    # Atributo de clase
    genero = 'Canis'
    id = 0  # contador de objetos de tipo perro

    # Comportamiento (Métodos)
    # Métodos especiales
    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        Perro.id += 1
        self.id = Perro.id

    def cumplir_anios(self):
        self.edad += 1

    def ladrar(self):
        return f'{self.nombre} dice guau guau.'

    def __str__(self):
        # f-strings
        return f'ID: {self.id} - {self.nombre} tiene {self.edad} años y su género es {self.genero}.'

# Prog. ppal
perro1 = Perro('Paka', 15)
print(type(perro1))
print(perro1)
perro2 = Perro('Paka', 15)
print(type(perro1))
print(perro2)
print(str(perro2))

perro1.cumplir_anios()
print(perro1.edad)
print(perro2.edad)
perro1.edad = 19
perro2.nombre = 'Firulais'
print(perro1.edad)

print(perro1)
print(perro2)

print(perro2.ladrar())
