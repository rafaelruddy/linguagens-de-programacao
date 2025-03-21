# 2. Contagem de Caracteres em uma Palavra
# Escreva um programa que solicite ao usuário uma palavra e utilize um dicionário
# para armazenar a contagem de cada caractere presente na palavra. Exiba o
# dicionário ao final.

palavra = input("Digite uma palavra: ")
dicionario = {}

for letra in palavra:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1

print("Contagem de caracteres:")
for letra, quantidade in dicionario.items():
    print(f"Letra: {letra}, Quantidade: {quantidade}")