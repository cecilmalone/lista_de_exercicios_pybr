"""
34. Os números primos possuem várias aplicações dentro da Computação, por
exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um
e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele
é ou não um número primo.
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