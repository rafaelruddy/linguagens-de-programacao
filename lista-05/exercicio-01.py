# 1. Cálculo do Fatorial
# Crie uma função que receba um número inteiro como parâmetro e retorne o seu
# fatorial. Em seguida, utilize essa função em um programa principal para calcular o
# fatorial de um número informado pelo usuário.

def calcular_fatorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

num = int(input("Digite um número: "))
fatorial = calcular_fatorial(num)
if fatorial is not None:
    print(f"O fatorial de {num} é {fatorial}")
else:
    print("O fatorial de um número negativo ou zero não existe.")