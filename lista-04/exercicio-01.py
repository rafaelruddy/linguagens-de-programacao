# 1. Soma dos Elementos de uma Lista
# Escreva um programa que solicite ao usuário uma lista de números inteiros e
# calcule a soma de todos os elementos da lista.

lista = []
while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    lista.append(num)

soma = sum(lista)
print("A soma dos elementos da lista é:", soma)