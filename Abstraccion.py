from abc import ABC, abstractmethod
import math
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado=lado
    def area(self):
        return self.lado*self.lado
    def perimetro(self):
        return self.lado * 4
class Circulo(Figura):
    def __init__(self,radio):
        self.radio=radio
    def area(self):
        return math.pi * self.radio * self.radio
    def perimetro(self):
        return 2 * math.pi *self.radio
c1=Cuadrado(5)
print(f"El area del cuadrado es : {c1.area()}")
print(f"El perimetro del cuadrado es : {c1.perimetro()}")

c2=Circulo(5)
print(f"El area del circulo es : {c2.area()}")
print(f"El perimetro del circulo es : {c2.perimetro()}")
        
        