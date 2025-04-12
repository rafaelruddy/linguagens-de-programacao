# 9. Herança e Polimorfismo
# Crie uma classe Animal com um método fazer_som(). Depois, crie duas subclasses
# Cachorro e Gato que sobrescrevem esse método para imprimir sons específicos de cada
# animal. No programa principal, crie objetos das classes e chame fazer_som().

class Animal:
    def fazer_som(self):
        pass
    
class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")
        
class Gato(Animal):
    def fazer_som(self):
        print("Miau!")
        
cachorro = Cachorro()

gato = Gato()

cachorro.fazer_som()

gato.fazer_som()