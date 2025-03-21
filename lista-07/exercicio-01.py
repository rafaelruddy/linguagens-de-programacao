# 1. Cadastro de Alunos
# Crie um programa que permita cadastrar alunos em um dicionário. O programa
# deve solicitar o nome e a nota do aluno e armazená-los como chave e valor no
# dicionário. Após a inserção de pelo menos 3 alunos, exiba a lista de alunos e suas
# respectivas notas.

alunos = {}

for i in range(3):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    alunos[nome] = nota

print("Lista de alunos e notas:")
for aluno, nota in alunos.items():
    print(f"Aluno: {aluno}, Nota: {nota}")