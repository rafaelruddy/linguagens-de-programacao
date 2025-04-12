# 12. Closures
# Implemente uma função multiplicador(fator) que recebe um número fator e
# retorna uma função que multiplica qualquer número por esse fator. Teste a função no
# programa principal.

def multiplicador(fator):
    def multiplicar(n):
        return n * fator
    return multiplicar

fator = float(input("Digite um fator: "))

multiplicar = multiplicador(fator)

n = float(input("Digite um número: "))

print(f"Resultado: {multiplicar(n)}")