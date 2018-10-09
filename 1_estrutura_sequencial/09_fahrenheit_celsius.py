"""
9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""

fahrenheit = float(input('Informe o valor em Fahrenheit (ºF): '))
celsius = (5 * (fahrenheit - 32) / 9)

print('{} ºF é igual a {:.1f} ºC'.format(fahrenheit, celsius))
