"""
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho 
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta 
a serem compradas e o preço total.
"""

metros_quadrados = int(input())
valor_lata = 80
lata_metro_quadrado = 18 / 3

quantidade_latas = metros_quadrados / lata_metro_quadrado

if quantidade_latas < 1:
    print(valor_lata)
else:
    total = quantidade_latas * valor_lata
    print(total)
