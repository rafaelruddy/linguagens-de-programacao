# 2. Operações Matemáticas com Números em uma Tupla
# Solicite ao usuário quatro números inteiros e armazene-os em uma tupla. Em
# seguida, exiba:
# • Quantas vezes o número 9 apareceu na tupla.
# • Em que posição foi digitado o primeiro número 3 (caso exista).
# • Os números pares contidos na tupla.

numeros = tuple(map(int, input("Digite quatro números inteiros: ").split()))

quantidade_nove = numeros.count(9)
posicao_primeiro_tres = numeros.index(3) if 3 in numeros else -1
numeros_pares = [num for num in numeros if num % 2 == 0]

print(f"Quantidade de vezes que o número 9 aparece na tupla: {quantidade_nove}")
print(f"Posição do primeiro número 3 na tupla: {posicao_primeiro_tres}")
print(f"Números pares na tupla: {numeros_pares}")