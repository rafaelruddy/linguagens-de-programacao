# 1. Divisão Segura
# Crie um programa que solicite ao usuário dois números e realize a divisão do
# primeiro pelo segundo. Utilize tratamento de exceções para evitar erros de
# divisão por zero e erros de entrada inválida (como caracteres não numéricos).

def dividir_seguro(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero"
    except ValueError:
        return "Erro: Entrada inválida"

# Solicita ao usuário dois números
dividendo = float(input("Digite o dividendo: "))
divisor = float(input("Digite o divisor: "))

# Realiza a divisão
resultado = dividir_seguro(dividendo, divisor)
print(f"Resultado: {resultado}")