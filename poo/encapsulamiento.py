class Perro:
    def __init__(self, nombre, raza):
        self.__nombre = nombre # Atributo privado
        self.__raza = raza
        
    def ladrar(self):
        print(f'{self.__nombre} esta ladrando!')
        
if __name__ == '__main__':
    mi_perro = Perro('Max', 'Labrador')
    mi_perro.ladrar() # Podemos llamar al método ladrar
    
# Intentar acceder directamente al atributo privado causará un error
# print (mi_perro.__nombre) ## esto no funcionará

    mi_perro.__nombre

'''
Traceback (most recent call last):
  File "/home/drs/python302/poo/encapsulamiento.py", line 16, in <module>
    mi_perro.__nombre
AttributeError: 'Perro' object has no attribute '__nombre'
'''
