# 4. Números Ímpares em um Intervalo
# Peça ao usuário dois números inteiros, representando um intervalo A,B. O programa deve
# exibir todos os números ímpares dentro desse intervalo (inclusive os limites, se forem
# ímpares).

a = int(input("Digite o intervalo A: "))
b = int(input("Digite o intervalo B: "))

for i in range(a, b + 1):
    if i % 2 != 0:
        print(i)