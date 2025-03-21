# 3. Dicionário de Tradução
# Crie um dicionário que contenha algumas palavras em português como chave e
# suas respectivas traduções para inglês como valor. Permita que o usuário digite
# uma palavra em português e retorne sua tradução. Caso a palavra não esteja no
# dicionário, exiba uma mensagem informando que a tradução não foi encontrada.

dicionario = {
    "ola": "hello",
    "mundo": "world",
    "bom dia": "good morning",
    "boa tarde": "good afternoon",
    "boa noite": "good night"
}

palavra = input("Digite uma palavra em português: ")

if palavra in dicionario:
    traducao = dicionario[palavra]
    print(f"Tradução para inglês: {traducao}")
else:
    print("Tradução nao encontrada.")