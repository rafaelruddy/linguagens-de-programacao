# 5. Conversão de Temperatura
# Crie uma função que converta temperaturas de Celsius para Fahrenheit. No
# programa principal, solicite uma temperatura ao usuário em graus Celsius e utilize
# a função para exibir o valor correspondente em Fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"A temperatura em Fahrenheit é: {fahrenheit}")