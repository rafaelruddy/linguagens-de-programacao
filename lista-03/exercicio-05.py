# 5. Sequência de Fibonacci
# Escreva um programa que peça ao usuário um número N e exiba os N primeiros termos da
# Sequência de Fibonacci.
# Obs: A sequência de Fibonacci começa com 0 e 1, e cada termo seguinte é a soma dos dois
# anteriores:

n = int(input("Digite um número: "))

a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b

    
