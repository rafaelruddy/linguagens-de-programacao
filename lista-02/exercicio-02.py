# 2. Maior Número
# Faça um programa que peça dois números ao usuário e exiba o maior deles. Caso os números
# sejam iguais, exiba uma mensagem informando essa condição.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro número é maior.")
elif num2 > num1:
    print("O segundo número é maior.")
else:
    print("Os dois números são iguais.")