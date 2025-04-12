# Módulo 1 - Módulos, Pacotes e PIP
# 1. Importação de Módulos
# Escreva um programa que importe os módulos math e random e use suas funções para:
# • Calcular a raiz quadrada de um número informado pelo usuário.
# • Gerar um número aleatório entre 1 e 100.

import math
import random

numero = float(input("Digite um número: "))

print(f"A raiz quadrada de {numero} é {math.sqrt(numero)}.")

print(f"Número aleatório entre 1 e 100: {random.randint(1, 100)}.")