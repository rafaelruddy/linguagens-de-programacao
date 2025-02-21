# 1. Par ou Ímpar?
# Escreva um programa que solicite um número inteiro ao usuário e informe se ele é par ou
# ímpar.

num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")