"""
10. Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos 
pelos elementos intercalados dos dois outros vetores.
"""

count = 1
vetor_a = []
vetor_b = []
vetor_c = []

while count <= 10:
    numero = float(input("Informe os números do grupo 1: "))
	vetor_a.append(numero)
	count += 1
	
while count <= 10:
    numero = float(input("Informe os números do grupo 2: "))
	vetor_b.append(numero)
	count += 1
	
for x in range(len(vetor_a):
    vetor_c.append(vetor_a[x])
	vetor_c.append(vetor_b[x])
	
print(vetor_a)
print(vetor_b)
print(vetor_c)
