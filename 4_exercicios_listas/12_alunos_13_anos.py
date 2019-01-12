"""
12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que 
determine quantos alunos com mais de 13 anos possuem altura inferior à média 
de altura desses alunos.
"""

dados = []
media = 0
alunos = 0

count = 1
while count <= 30:
    idade, altura = input("Informe a idade e altura: ").split()
    idade, altura = int(idade), float(altura)
    dados.append([idade, altura])

for i in range(len(dados)):
	media += dados[i][1]

media = media / len(dados)

for i in range(len(dados)):
	if (dados[i][1] < media) and (dados[i][0] > 13):
		alunos += 1 

print("Há {} alunos que possuem mais de 13 e são menor que a média de altura dos alunos.".format(alunos))