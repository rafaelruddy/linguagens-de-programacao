# 5. Operações Bancárias com Tratamento de Erros
# Crie um programa que simule um sistema bancário simples. O saldo inicial do
# usuário é de R$ 1000,00. O programa deve permitir que o usuário insira um valor
# para saque e, caso o valor solicitado seja maior que o saldo disponível, uma
# exceção personalizada deve ser lançada informando que o saldo é insuficiente.

saldo = 1000

valor_saque = float(input("Digite o valor do saque: "))

try:
    if valor_saque > saldo:
        raise ValueError("Saldo insuficiente")
except ValueError as e:
    print(e)



