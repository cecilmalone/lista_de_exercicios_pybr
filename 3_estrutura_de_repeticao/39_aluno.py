"""
39. Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando a sua altura em
centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do
aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

alunos = []
codigo = 1

while codigo <= 10:
    codigo, altura = input("Informe o codigo e altura do aluno: ").split()
    codigo, altura = int(codigo), float(altura)
    alunos.append({'Código': codigo, 'Altura': altura})
    codigo += 1

mais_alto = -1
mais_baixo = 999
mais_gordo = -1
mais_magro = 999
total_altura = 0
total_peso = 0

for aluno in alunos:
    if aluno['Altura'] > mais_alto:
        codigo_mais_alto = aluno['Código']
        mais_alto = aluno['Altura']
    if aluno['Altura'] < mais_baixo:
        codigo_mais_baixo = aluno['Código']
        mais_baixo = aluno['Altura']

print("O aluno de número {} é o mais alto, possuindo a altura de {}m de altura"
      .format(codigo_mais_alto, mais_alto))
print("O aluno de número {} é o mais baixo, possuindo a altura de {}m de altura"
      .format(codigo_mais_baixo, mais_baixo))

