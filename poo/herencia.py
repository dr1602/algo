# Herencia

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def comer(self):
        print(f'{self.nombre} esta comiendo')
        
class Perro(Animal):
    def ladrar(self):
        print(f'{self.nombre} esta ladrando!')
        
if __name__ == '__main__':
    mi_perro = Perro('Inu')
    mi_perro.comer() # Hereda el metodo comer de la clase animal
    '''
    Inu esta comiendo
    '''
    mi_perro.ladrar() # Metodo especifico de la clase Perro
    '''
    Inu esta ladrando!
    '''
    