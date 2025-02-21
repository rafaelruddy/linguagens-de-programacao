# 4. Cálculo do Salário Mensal
# Faça um programa que pergunte o número de horas trabalhadas no mês e o valor recebido
# por hora. O programa deve calcular e exibir o salário total do mês.

horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
valor_hora = float(input("Digite o valor recebido por hora: "))

salario_mensal = horas_trabalhadas * valor_hora

print(f"O salário mensal é: R${salario_mensal:.2f}")