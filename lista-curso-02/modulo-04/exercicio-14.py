# 14. Processamento de Arquivos Binários
# Escreva um programa que crie um arquivo binário dados.bin e grave uma lista de
# números inteiros nele. Em seguida, abra o arquivo e exiba os números armazenados.

numeros = [1, 2, 3, 4, 5]

with open("dados.bin", "wb") as arquivo:
    for numero in numeros:
        arquivo.write(numero.to_bytes(4, "little"))
        
with open("dados.bin", "rb") as arquivo:
    while True:
        byte = arquivo.read(4)
        if not byte:
            break
        print(int.from_bytes(byte, "little"))