# 3. Listagem de Cores do Arco-Íris
# Crie uma tupla contendo as cores do arco-íris em ordem. Depois, permita que o
# usuário informe um número de 1 a 7 e exiba a cor correspondente.

cores = ("Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta")

numero = int(input("Digite um número de 1 a 7: "))

if 1 <= numero <= 7:
    cor = cores[numero - 1]
    print(f"A cor correspondente ao número {numero} é: {cor}")
else:
    print("O número deve estar entre 1 e 7.")