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

metros_quadrados = int(input('Informe o tamanho em metros quadrados da área a ser pintada: '))

litro_lata = 18
valor_lata = 80
lata_metro_quadrado = 18 / 6

litro_galao = 3.6
valor_galao = 25
galao_metro_quadrado = 3.6 / 6

quantidade_latas = metros_quadrados / lata_metro_quadrado
quantidade_galoes = metros_quadrados / galao_metro_quadrado

if quantidade_latas <= 1:
    quantidade_latas = 1
    print('Comprando apenas latas de 18 litros')
    print('Quantidade de latas: %d' % quantidade_latas)
    print('Preço total: %.2f' % valor_lata)
else:
    total = quantidade_latas * valor_lata
    print('Comprando apenas latas de 18 litros')
    print('Quantidade de latas: %d' % quantidade_latas)
    print('Preço total: %.2f' % total)

if quantidade_galoes <= 1:
    quantidade_galoes = 1
    print('Comprando apenas galões de 3,6 litros')
    print('Quantidade de latas: %d' % quantidade_galoes)
    print('Preço total: %.2f' % valor_galao)
else:
    total = quantidade_galoes * valor_galao
    print('Comprando apenas galões de 3,6 litros')
    print('Quantidade de latas: %d' % quantidade_galoes)
    print('Preço total: %.2f' % total)


a1 = int(litrosf/18)
        a2 = litrosf%18
        a3 = math.ceil(a2/3.6)
        a4 = ((a1*80)+(a3*25))
        print("Você de %d litros de tinta, %d latas, %d galões e pagará R$ %d" % (litrosf,a1,a3,a4))
quantidade_ideal = 0


