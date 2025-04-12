# 4. Processamento de Strings
# Peça ao usuário para digitar uma frase e implemente funções para:
# • Contar quantas vezes cada vogal aparece na frase.
# • Exibir a frase ao contrário.
# • Substituir todos os espaços por -.

def processar_frase():
    frase = input("Digite uma frase: ")
    vogais = "aeiou"
    for vogal in vogais:
        print(f"A vogal {vogal} aparece {frase.lower().count(vogal)} vezes.")
    print(f"Frase ao contrário: {frase[::-1]}")
    print(f"Frase com espaços substituídos por -: {frase.replace(' ', '-')}")
    
processar_frase()