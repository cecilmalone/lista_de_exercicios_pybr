"""
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

n1 = int(input("Informe um número: "))
n2 = int(input("Informe um número: "))
n3 = int(input("Informe um número: "))

if(n3 > n2):
    aux = n3
    n3 = n2
    n2 = aux

if(n2 > n1):
    aux = n2
    n2 = n1
    n1 = aux

if(n3 > n2):
    aux = n3
    n3 = n2
    n2 = aux

print("A ordem decrescente dos números são {} {} {}".format(n1, n2, n3))