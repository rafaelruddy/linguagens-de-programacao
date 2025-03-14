# 2. Verificação de Número Primo
# Crie uma função que receba um número inteiro e retorne True se for primo e False
# caso contrário. No programa principal, solicite um número ao usuário e utilize a
# função para verificar se ele é primo.

def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Digite um número: "))
if eh_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")

