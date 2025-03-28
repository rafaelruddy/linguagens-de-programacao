# 4. Acesso a Elementos de uma Lista
# Crie uma lista com cinco números e permita que o usuário informe um índice para
# acessar um valor da lista. Utilize tratamento de exceções para evitar erros caso o
# usuário digite um índice inválido.

lista = [1, 2, 3, 4, 5]

indice = int(input("Digite um índice para acessar um valor da lista: "))

try:
    print(lista[indice])
except IndexError:
    print("Erro: Índice inválido. Digite um índice válido.")

