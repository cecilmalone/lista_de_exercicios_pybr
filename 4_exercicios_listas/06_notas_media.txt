"""
6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene 
num vetor a média de cada aluno, imprima o número de alunos com média maior 
ou igual a 7.0.
"""

count = 1
medias = []

while count <= 20:
    notas = []
	notas = input("Informe as notas: ").split()
	notas = [float(x) for x in notas]
		
	media = sum(notas) / len(notas)
	medias.append(media)
	
	count += 1

for x in medias:
    if x >= 7:
	    print(x, end=', ')
