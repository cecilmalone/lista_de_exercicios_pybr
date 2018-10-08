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

metros_quadrados = int(input())

litro_lata = 18
valor_lata = 80
lata_metro_quadrado = 18 / 6

litro_galao = 3.6
valor_galao = 25
galao_metro_quadrado = 3.6 / 6


quantidade_latas = metros_quadrados / lata_metro_quadrado
quantidade_galoes = metros_quadrados / galao_metro_quadrado
quantidade_ideal = 0


