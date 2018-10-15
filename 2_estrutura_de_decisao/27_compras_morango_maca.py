"""
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra 
    ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
    Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a 
    quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo 
    cliente.
"""

morango_quilos = float(input("Informe a quantidade (em Kg) de Morangos: "))
macas_quilos = float(input("Informe a quantidade (em Kg) de Maças: "))

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

print("Valor a ser pago: R$ {:.2f}".format(valor_compra))
