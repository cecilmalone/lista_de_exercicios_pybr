"""
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho 
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta 
a serem compradas e o preço total.
"""

import math

metros_quadrados = int(input('Informe o tamanho em metros quadrados da área a ser pintada: '))
litros = metros_quadrados / 3

valor_lata = 80.0
capacidade_litros = 18

quantidade_latas = litros / capacidade_litros
total = math.floor(quantidade_latas) * valor_lata

if quantidade_latas <= 1:
    print('Quantidade de latas: 1')
    print('Preço total: %.2f' % valor_lata)
else:
    print('Quantidade de latas: %d' % quantidade_latas)
    print('Preço total: %.2f' % total)
