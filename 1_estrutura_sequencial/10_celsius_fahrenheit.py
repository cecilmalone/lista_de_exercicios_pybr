"""
10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
"""

celsius = float(input('Informe o valor em Celsius (ºC): '))
fahrenheit = (celsius * (9/5)) + 32

print('{} ºC é igual a {:.1f} ºF'.format(celsius, fahrenheit))
