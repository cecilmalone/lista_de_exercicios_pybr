"""
32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120
"""

numeros = []
resultado = 1

numero = int(input("Informe um número: "))

print("Fatorial de: {}".format(numero))
for x in range(1, numero + 1):
    numeros.append(x)
    resultado *= x

numeros = [int()]
print("{}! = {} = {}".format(numero, numeros[::-1], resultado))
