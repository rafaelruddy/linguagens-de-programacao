# 5. Manipulação de Listas e Strings
# Solicite ao usuário que insira uma lista de palavras separadas por espaço. Em seguida,
# exiba:
# • A lista ordenada alfabeticamente.
# • O número total de palavras.
# • As palavras convertidas para maiúsculas.

def manipular_lista():
    palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
    palavras.sort()
    print("Lista ordenada alfabeticamente:"," ".join(palavras))
    
    print(f"Número total de palavras: {len(palavras)}")
    
    print("Palavras convertidas para maiúsculas:", end=" ")
    
    for palavra in palavras:
        print(palavra.upper(), end=" ")
        
    print()
    
manipular_lista()