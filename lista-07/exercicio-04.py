# 4. Estatísticas de um Texto
# Peça ao usuário para inserir uma frase. Utilize um dicionário para armazenar a
# contagem de palavras, ou seja, a chave será a palavra e o valor será o número de
# vezes que ela aparece na frase. Exiba o dicionário ao final.

frase = input("Digite uma frase: ")
palavras = frase.split()
dicionario = {}

for palavra in palavras:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

print("Contagem de palavras:")
for palavra, quantidade in dicionario.items():
    print(f"Palavra: {palavra}, Quantidade: {quantidade}")