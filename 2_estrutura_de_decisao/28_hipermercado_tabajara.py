"""
28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. 
Confira:
                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
    Para atender a todos os clientes, cada cliente poderá levar apenas um dos 
    tipos de carne da promoção, porém não há limites para a quantidade de carne 
    por cliente. Se compra for feita no cartão Tabajara o cliente receberá 
    ainda um desconto de 5% sobre o total da compra. Escreva um programa que 
    peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom 
    fiscal, contendo as informações da compra: tipo e quantidade de carne, preço 
    total, tipo de pagamento, valor do desconto e valor a pagar.
"""

tipo_carne = input("Qual o tipo da carne: ")
quilos = float(input("Informe a quantidade (em Kg) de Carne: "))
forma_pagamento = input("Qual a forma de pagamento: ")

if morango_quilos <= 5:
    valor_morango = morango_quilos * 2.50
else:
    valor_morango = morango_quilos * 2.20

if macas_quilos <= 5:
    valor_maca = macas_quilos * 1.80
else:
    valor_maca = macas_quilos * 1.50

valor_compra = valor_morango + valor_maca

if (morango_quilos + macas_quilos) > 8 or valor_compra > 25:
    valor_compra = valor_compra - (valor_compra * 0.10)

print("Tipo da Carne: {}".format(tipo_carne))
print("Quantidade de Carne (Kg): {}".format(quilos))
print("Preço Total: R$ {}".format(teste))
print("Forma de Pagamento: R$ {}".format(forma_pagamento))
print("Valor do Desconto: R$ {:.2f}".format(valor_compra))
print("Valor a pagar: R$ {:.2f}".format(valor_compra))
