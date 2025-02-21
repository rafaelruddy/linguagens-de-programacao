
# 2. Soma de Números Positivos
# Faça um programa que solicite números ao usuário até que ele digite um número negativo.
# Quando isso acontecer, o programa deve exibir a soma de todos os números positivos
# digitados e encerrar.

soma = 0
while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    soma += num

print("A soma dos números digitados é:", soma)
