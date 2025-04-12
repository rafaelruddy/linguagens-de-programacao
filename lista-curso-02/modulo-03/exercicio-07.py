# 7. Criando uma Classe Carro
# Implemente uma classe Carro com os atributos marca, modelo e ano. A classe deve ter
# um método exibir_detalhes() que imprime essas informações. No programa
# principal, crie dois objetos da classe e exiba seus detalhes.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def exibir_detalhes(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}")
        
carro1 = Carro("Chevrolet", "Onix", 2021)
carro2 = Carro("Fiat", "Uno", 2019)

carro1.exibir_detalhes()

carro2.exibir_detalhes()