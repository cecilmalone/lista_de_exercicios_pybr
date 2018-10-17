"""
17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo 
usuário. Ex.: 5!=5.4.3.2.1=120
"""

numero = int(input("Informe um número: "))
resultado = 1
lista = []

for x in range(numero):
    resultado *= x
    lista.append(resultado)

for y in range(len(lista)):
    print("{}!={}={}".format(numero, lista[::-1], resultado))
