class Animal:
    def hacer_sonido(self):
        pass
    
class Perro(Animal):
    def hacer_sonido(self):
        print('¡Guau!')
        
class Gato(Animal):
    def hacer_sonido(self):
        print('¡Miau!')
        
if __name__ == '__main__':
    # Creamos objetos de diferentes clases
    perro = Perro()
    gato = Gato()
    
    # Llamamos al mismo método para cada objeto
    perro.hacer_sonido()
    gato.hacer_sonido()
