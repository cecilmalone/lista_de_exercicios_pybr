"""
27. Faça um programa que calcule o número médio de alunos por turma. Para isto, 
peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas 
não podem ter mais de 40 alunos.
"""

turmas = int(input("Informe a quantidade de turmas: "))

alunos = []

for x in range(turmas): 
    qtd_alunos = int(input("Informe a quantidade de alunos na turma {}: ".format(x))
    while qtd_alunos > 40:
        qtd_alunos = int(input("Informe a quantidade de alunos na turma {}: ".format(x))
    alunos.append(qtd_alunos)

total = 0

for n in alunos:
    total += n

print("A média de alunos por tuma é igual a {}".format(total / len(alunos)))
