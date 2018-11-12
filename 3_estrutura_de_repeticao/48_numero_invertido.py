"""
48. Faça um programa que peça um numero inteiro positivo e em seguida mostre 
este numero invertido.
    Exemplo:
      12376489
      => 98467321
"""

numero = int(input("Informe um número a ser invertido: "))

numero = numero[::-1]

print("=> {}".format(numero))
