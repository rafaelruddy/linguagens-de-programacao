# 11. Iteradores
# Crie uma classe Contador que implemente um iterador que conta de 1 até n. No
# programa principal, percorra os valores utilizando for.

class Contador:
    def __init__(self, n):
        self.n = n
        self.i = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        self.i += 1
        if self.i <= self.n:
            return self.i
        else:
            raise StopIteration
        
n = int(input("Digite um número: "))

for i in Contador(n):
    print(i, end=" ")
print()