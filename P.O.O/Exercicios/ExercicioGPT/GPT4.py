from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        ...

class QuadradoArea(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        area = self.lado ** 2
        print(f"A area do quadrado de lado {self.lado} é {area}")

class CirculoArea(FormaGeometrica):
    def __init__(self,raio):
        self.raio = raio
    def calcular_area(self):
        area = math.pi*self.raio*self.raio
        print(f"A área do circulo de raio {self.raio} é {area}") 
    
Quadrado1 = QuadradoArea(20)
Quadrado1.calcular_area()

Circulo1 =  CirculoArea(2)
Circulo1.calcular_area()