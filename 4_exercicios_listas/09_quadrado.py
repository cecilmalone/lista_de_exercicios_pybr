"""
9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e 
mostre a soma dos quadrados dos elementos do vetor.
"""

count = 1
numeros = []
soma = 0

while count <= 10:
    numero = int(input("Informe a nota: "))
	numeros.append(numero)
	
	count += 1
	
for x in numeros:
    soma += x ** 2

print("Soma dos quadrados: {}".format(soma))
