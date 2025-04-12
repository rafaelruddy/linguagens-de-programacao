# 3. Criando e Usando um Módulo Personalizado
# Crie um módulo chamado meu_modulo.py contendo uma função dobro(n) que retorna
# o dobro de um número. Depois, escreva um programa principal que importe esse
# módulo e utilize a função.

import meu_modulo

numero = float(input("Digite um número: "))

print(f"O dobro de {numero} é {meu_modulo.dobro(numero)}.")