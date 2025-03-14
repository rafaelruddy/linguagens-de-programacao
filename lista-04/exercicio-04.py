# 4. Inverter a Lista
# Escreva um programa que leia uma lista de palavras e exiba essa lista na ordem
# inversa.

palavras = []
while True:
    palavra = input("Digite uma palavra (ou 0 para sair): ")
    if palavra == "0":
        break
    palavras.append(palavra)

palavras_invertidas = palavras[::-1]

print("Lista invertida:", palavras_invertidas)