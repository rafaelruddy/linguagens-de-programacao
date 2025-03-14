# 3. Cálculo da Média de uma Lista
# Crie uma função que receba uma lista de números e retorne a média dos valores.
# No programa principal, peça ao usuário para inserir os números e exiba a média
# utilizando a função criada.

def calcular_media(lista):
    return sum(lista) / len(lista)

numeros = []
while True:
    num = float(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    numeros.append(num)

media = calcular_media(numeros)

print(f"A média dos números é: {media}")