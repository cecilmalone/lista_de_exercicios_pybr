"""
21. Faça um programa que peça um número inteiro e determine se ele é ou não um 
número primo. Um número primo é aquele que é divisível somente por ele mesmo e 
por 1.
"""

numero = int(input("Informe um número: "))
tot = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        tot += 1

if tot == 2:
    print("O número {} é primo.".format(numero))
else:
    print("O número {} não é primo.".format(numero))
