"""
24. Faça um programa que calcule o mostre a média aritmética de N notas.
"""

numeros = []
soma = 0

numeros = input("Informe as notas: ")
numeros = [int(x) for x in numeros]

for x in numeros:
    soma += x

media = soma / len(numeros)

print("A média das notas informadas é", media)
