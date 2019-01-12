"""
8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada 
informação no seu respectivo vetor. Imprima a idade e a altura na ordem 
inversa a ordem lida.
"""

count = 1
idades = []
alturas = []

while count <= 5:
    idade = int(input("Informe a idade: "))
	idades.append(idade)
	altura = float(input("Informe a altura: "))
	alturas.append(altura)

	count += 1

print("Idades invertidas: {}".format(idades[::-1]))
print("Alturas invertidas: {:.2f}".format(alturas[::-1]))
