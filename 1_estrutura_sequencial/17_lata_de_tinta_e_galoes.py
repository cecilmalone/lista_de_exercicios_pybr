"""
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho 
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        comprar apenas latas de 18 litros;
        comprar apenas galões de 3,6 litros;
        misturar latas e galões, de forma que o preço seja o menor. Acrescente
        10% de folga e sempre arredonde os valores para cima, isto é, considere 
        latas cheias.
"""

import math

metros_quadrados = int(input('Informe o tamanho em metros quadrados da área a ser pintada: '))
metros_lata = metros_quadrados / 6

if (metros_lata <= 0):
    metros_lata = 1

quantidade_latas_18 = math.floor(metros_lata / 18 + (18 * 0.10))
quantidade_galoes_36 = math.floor(metros_lata / 3.6 + (3.6 * 0.10))
qtd_latas = metros_lata / 18
resto = metros_lata % 18

if (resto > 0 and resto <= 3.6):
    qtd_galoes = 1
elif (resto == 0):
    qtd_galoes = 0
else:
    qtd_galoes = math.floor(resto / 3.6 + (3.6 * 0.10))

if (quantidade_latas_18 <= 0 or quantidade_galoes_36 <= 0 or qtd_galoes < 0):
    quantidade_latas_18 = 1
    quantidade_galoes_36 = 1
    qtd_galoes = 1


preco_latas_18 = quantidade_latas_18 * 80
preco_galoes_36 = quantidade_galoes_36 * 25
preco_latas = qtd_latas * 80
preco_galoes = qtd_galoes * 25

preco_otimo = preco_latas + preco_galoes
 
print('Comprando apenas latas de 18 litros')
print('Quantidade de latas: %d' % quantidade_latas_18)
print('Preço total: %.2f' % preco_latas_18)
print()
print('Comprando apenas galões de 3,6 litros')
print('Quantidade de galões: %d' % quantidade_galoes_36)
print('Preço total: %.2f' % preco_galoes_36)
print()
print('Misturando latas e galões, de forma que o preço seja o menor')
print('Quantidade de latas: %d' % qtd_latas)
print('Quantidade de galões: %d' % qtd_galoes)
print('Preço total: %.2f' % preco_otimo)
