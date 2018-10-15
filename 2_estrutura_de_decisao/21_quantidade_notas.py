"""
21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao 
usuário a valor do saque e depois informar quantas notas de cada valor serão 
fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor 
mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar 
com a quantidade de notas existentes na máquina.
    a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas 
    notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três 
    notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro 
    notas de 1.
"""

import math

saque = float(input("Informe o valor do saque: "))
while (saque < 10) and (saque > 600):
    saque = float(input("Informe o valor do saque"))

notas_100 = math.floor(saque / 100)
resto = saque - (notas_100 * 100)
notas_50 = math.floor(resto / 50)
resto = resto - (notas_50 * 50)
notas_10 = math.floor(resto / 10)
resto = resto - (notas_10 * 10)
notas_5 = math.floor(resto / 5)
resto = resto - (notas_5 * 5)
notas_1 = math.floor(resto / 1)
resto = resto - (notas_1 * 1)

print("Para o valor de R$ {}, o sistema irá emitir as seguintes notas e quantidades: ".format(saque))
print("R$ 100,00: {}".format(notas_100))
print("R$ 50,00: {}".format(notas_50))
print("R$ 10,00: {}".format(notas_10))
print("R$ 5,00: {}".format(notas_5))
print("R$ 1,00: {}".format(notas_1))
