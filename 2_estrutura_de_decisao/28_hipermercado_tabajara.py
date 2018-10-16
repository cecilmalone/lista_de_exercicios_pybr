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

if tipo_carne == "File Duplo":
    if quilos <= 5:
        preco_total = quilos * 4.90
    else:
        preco_total = quilos * 5.80
elif tipo_carne == "Alcatra":
    if quilos <= 5:
        preco_total = quilos * 5.90
    else:
        preco_total = quilos * 6.80
elif tipo_carne == "Picanha":
    if quilos <= 5:
        preco_total = quilos * 6.90
    else:
        preco_total = quilos * 7.80

if forma_pagamento == "Cartão Tabajara":
    desconto = preco_total * 0.05

print("Tipo da Carne: {}".format(tipo_carne))
print("Quantidade de Carne (Kg): {}".format(quilos))
print("Preço Total: R$ {}".format(preco_total))
print("Forma de Pagamento: {}".format(forma_pagamento))
print("Valor do Desconto: R$ {:.2f}".format(desconto))
print("Valor a pagar: R$ {:.2f}".format(preco_total - desconto))
