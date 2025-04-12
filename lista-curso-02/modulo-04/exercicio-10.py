# 10. Geradores
# Implemente um gerador chamado contar_pares(n) que gera números pares até n. No
# programa principal, utilize for para exibir os números pares até um valor inserido pelo
# usuário.

def contar_pares(n):
    for i in range(2, n + 1, 2):
        yield i
        
n = int(input("Digite um número: "))
for i in contar_pares(n):
    print(i, end=" ")
print()