# 13. Processamento de Arquivos de Texto
# Crie um programa que leia um arquivo chamado dados.txt, conte quantas linhas ele
# possui e exiba o conteúdo na tela.

with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(f"O arquivo possui {len(linhas)} linhas.")
    for linha in linhas:
        print(linha, end="")