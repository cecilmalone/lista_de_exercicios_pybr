"""
18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

numeros = []

numeros = input("Informe um conjunto de números: ").split()

maior = max(numeros)
menor = min(numeros)

for x in numeros:
    soma =+ x

print("Maior valor:", maior)
print("Menor valor:", menor)
print("Soma dos valores:", soma)
