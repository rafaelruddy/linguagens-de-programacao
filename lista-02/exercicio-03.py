# 3. Classificação de Idade
# Crie um programa que peça a idade de uma pessoa e informe sua classificação:
# • Menor de idade (menos de 18 anos)
# • Adulto (entre 18 e 59 anos)
# • Idoso (60 anos ou mais)

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")