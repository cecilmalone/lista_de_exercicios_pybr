"""
7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a 
multiplicação e os números.
"""

count = 1
numeros = []
soma = 0
multiplicacao = 1

while count <= 5:
    numero = int(input("Informe as notas: "))
	numeros.append(numero)
	
	count += 1

for numero in numeros:
    soma += numero
	multiplicacao *= numero
	
print("Soma: {}".format(soma))
print("Multiplicação: {}".format(multiplicacao))
print("Números: {}".format(numeros))
