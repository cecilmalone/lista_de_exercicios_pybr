"""
9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""

fahrenheit = float(input())
celsius = (5 * (fahrenheit - 32) / 9)

print(celsius)