from abc import ABC, abstractclassmethod

class Forma(ABC):
    @abstractclassmethod
    def calcular_area(self):
        pass
    
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return 3.14159265359 * self.radio**2
    
if __name__ == '__main__':
    circulo = Circulo(5)
    print(circulo.calcular_area())