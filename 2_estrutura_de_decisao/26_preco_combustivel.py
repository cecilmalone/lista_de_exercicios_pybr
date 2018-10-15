"""
26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    a. Álcool:
    b. até 20 litros, desconto de 3% por litro
    c. acima de 20 litros, desconto de 5% por litro
    d. Gasolina:
    e. até 20 litros, desconto de 4% por litro
    f. acima de 20 litros, desconto de 6% por litro 
    Escreva um algoritmo que leia o número de litros vendidos, o tipo de 
    combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule 
    e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro 
    da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
preco_litro_gasolina = 2.50
preco_litro_alcool = 1.90

litros = float(input("Informe a quantidade de litros vendidos: "))
tipo_combustivel = float(input("Informe o tipo do combustível: "))

if tipo_combustivel.upper() == 'A' or tipo_combustivel == 'álcool':
    if litros <= 20:
        valor_normal = preco_litro_alcool * litros
        valor_desconto = valor_normal - (valor_normal * 0.03)
        print("Valor a ser pago: R$ {:.2f}".format(valor_desconto))
    else:
        valor_normal = preco_litro_alcool * litros
        valor_desconto = valor_normal - (valor_normal * 0.05)
        print("Valor a ser pago: R$ {:.2f}".format(valor_desconto))
elif tipo_combustivel.upper() == 'G' or tipo_combustivel == 'gasolina':
    if litros <= 20:
        valor_normal = preco_litro_gasolina * litros
        valor_desconto = valor_normal - (valor_normal * 0.04)
        print("Valor a ser pago: R$ {:.2f}".format(valor_desconto))
    else:
        valor_normal = preco_litro_gasolina * litros
        valor_desconto = valor_normal - (valor_normal * 0.06)
        print("Valor a ser pago: R$ {:.2f}".format(valor_desconto))
