"""
11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

vetor_a = []
vetor_b = []
vetor_c = []
vetor_d = []

count = 1
while count <= 10:
    numero = float(input("Informe os números do grupo 1: "))
	vetor_a.append(numero)
	count += 1

count = 1	
while count <= 10:
    numero = float(input("Informe os números do grupo 2: "))
	vetor_b.append(numero)
	count += 1
	
count = 1
while count <= 10:
    numero = float(input("Informe os números do grupo 3: "))
	vetor_c.append(numero)
	count += 1
	
for x in range(len(vetor_a):
    vetor_d.append(vetor_a[x])
	vetor_d.append(vetor_b[x])
	vetor_d.append(vetor_c[x])
	
print(vetor_a)
print(vetor_b)
print(vetor_c)
print(vetor_d)
