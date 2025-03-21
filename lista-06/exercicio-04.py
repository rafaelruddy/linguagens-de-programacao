# 4. Nomes de Alunos e Notas
# Crie uma tupla que armazene o nome de cinco alunos e suas respectivas notas
# (ex: ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)). Depois, exiba
# apenas os nomes dos alunos e, em seguida, apenas as notas.

alunos = ("Ana", 8.5, "Carlos", 7.0, "Beatriz", 9.2, "Daniel", 6.8, "Eduarda", 8.0)

nomes = [alunos[i] for i in range(0, len(alunos), 2)]
notas = [alunos[i] for i in range(1, len(alunos), 2)]

print("Nomes dos alunos:")
for nome in nomes:
    print(nome)

print("\nNotas dos alunos:")
for nota in notas:
    print(nota)