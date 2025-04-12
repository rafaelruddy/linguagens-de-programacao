# 6. Tratamento de Exceções
# Crie um programa que solicite ao usuário dois números e tente dividir o primeiro pelo
# segundo. O programa deve capturar exceções como ZeroDivisionError e ValueError
# e exibir mensagens apropriadas.

def tratar_excecoes():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {numero1 / numero2}")
            break
        except ZeroDivisionError:
            print("Erro: divisão por zero.")
        except ValueError:
            print("Erro: entrada inválida.")
            
tratar_excecoes()