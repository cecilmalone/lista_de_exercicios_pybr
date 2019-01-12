"""
5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
"""

count = 1
numeros = []
pares = []
impares = []

while count <= 20:
    numero = int(input("Informe a nota: "))
	numeros.append(numero)
	
	if numero % 2 == 0:
	    pares.append(numero)
	else:
	    impares.append(numero)
	
	count += 1

print("Números: {}".format(numeros))
print("Pares: {}".format(pares))
print("Ímpares: {}".format(impares))
