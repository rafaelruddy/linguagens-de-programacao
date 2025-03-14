# 3. Remover Duplicatas
# Escreva um programa que leia uma lista de números e remova os valores
# duplicados, mantendo a ordem original.

numeros = []
while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    numeros.append(num)

numeros_sem_duplicatas = list(set(numeros))

print("Lista sem duplicatas:", numeros_sem_duplicatas)