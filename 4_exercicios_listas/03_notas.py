"""
3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

count = 1
lista_notas = []

while count <= 4:
    nota = float(input("Informe a nota: "))
	lista_notas.append(notas)
	
	count += 1

for x in lista_notas:
    print("Nota {}: {:.f}".format(x + 1, lista_notas[x]))
	
print("Média: {}".format(sum(lista_notas) / len(lista_notas)))
