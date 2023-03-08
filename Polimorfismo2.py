"""class Perro():
    def moverse(self):
        print("El perro camina")
class Tiburon():
    def moverse(self):
        print("El tiburon nada")
class Serpiente():
    def moverse(self):
        print("La serpiente repta")
class Animal():
    def __init__(self,tipo_animal):
        self.tipo_animal=tipo_animal
        self.tipo_animal.moverse()
    def accion(self):
        self.tipo_animal.moverse()
Animal(Perro())
Animal(Tiburon())
Animal(Serpiente())
mianimal=Animal(Perro())
mianimal.accion()"""
class Perro:
    def hablar(self):
        print("Guau!")

class Gato:
    def hablar(self):
        print("Miau!")

class Vaca:
    def hablar(self):
        print("Muuu!")
def sonido(tipodesonido):
    tipodesonido.hablar()
felino=Gato()
sonido(felino)

        
