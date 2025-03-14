# 2. Encontrar o Maior e o Menor Número
# Escreva um programa que leia uma lista de números digitados pelo usuário e
# determine o maior e o menor número presentes na lista.

numeros = []
while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)

print("O maior número digitado é:", maior)
print("O menor número digitado é:", menor)