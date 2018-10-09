"""
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

prod_1 = float(input("Informe o preço do produto: "))
prod_2 = float(input("Informe o preço do produto: "))
prod_3 = float(input("Informe o preço do produto: "))

if (prod_1 > prod_2) and (prod_1 > prod_3):
    print("O produto mais barato custa R$ {}".format(prod_1))
elif (prod_2 > prod_1) and (prod_2 > prod_3):
    print("O produto mais barato custa R$ {}".format(prod_2))
else:
    print("O produto mais barato custa R$ {}".format(prod_3))
