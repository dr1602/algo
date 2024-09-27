class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def mostrar_info(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}')
        
# Subclase que hereda de Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, tipo_combustible):
        super().__init__(marca, modelo)
        self.tipo_combustible = tipo_combustible
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f'Combustible: {self.tipo_combustible}')
        
if __name__ == '__main__':
    from POO import Vehiculo, Coche
    
    mi_coche = Coche('Toyota', 'Corola', 'Gasolina')
    mi_coche.mostrar_info()
    
'''
Marca: Toyota, Modelo: Corola
Combustible: Gasolina
'''