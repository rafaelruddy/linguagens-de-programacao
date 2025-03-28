# 2. Abertura Segura de Arquivo
# Escreva um programa que solicite ao usuário o nome de um arquivo para leitura. O
# programa deve tentar abrir o arquivo e exibir seu conteúdo. Utilize tratamento de
# exceções para lidar com a ausência do arquivo e outros possíveis erros.

def abrir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:

nome_arquivo = input("Digite o nome do arquivo para leitura: ")
conteudo = abrir_arquivo(nome_arquivo)
print(conteudo)
