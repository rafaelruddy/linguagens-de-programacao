# 5. Contar Ocorrências de um Elemento
# Escreva um programa que peça ao usuário para inserir uma lista de números e um
# número específico. O programa deve contar quantas vezes esse número aparece
# na lista.

lista = []
while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    lista.append(num)

elemento = int(input("Digite o elemento que deseja contar: "))

ocorrencias = lista.count(elemento)

print(f"O elemento {elemento} aparece {ocorrencias} vezes na lista.")