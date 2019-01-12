"""
4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas 
consoantes foram lidas. Imprima as consoantes.
"""

count = 1
lista_caracteres = []
lista_consoantes = []

while count <= 10:
    caracter = input("Informe a nota: ")
	lista_caracteres.append(caracter)
	
	count += 1

for palavra in caracteres:
    for letra in palavra:
	    if letra not in ('a', 'e', 'i', 'o', 'u'):
		    lista_consoantes.append(letra)
		
print("Foram lidas no total {} consoantes.".format(len(lista_consoantes)
print("Foram encontradas as seguintes consoantes: {}".format(lista_consoantes)
