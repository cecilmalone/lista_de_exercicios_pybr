"""
23. Faça um Programa que peça um número e informe se o número é inteiro ou 
decimal. Dica: utilize uma função de arredondamento.
"""

import math

numero = float(input("Informe um número: "))

if round(numero) != numero:
    print("O número {} é decimal.".format(numero))
else:
    print("O número {} é inteiro.".format(numero))
