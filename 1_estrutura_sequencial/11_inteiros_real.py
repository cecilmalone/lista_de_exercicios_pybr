"""
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo.
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.
"""

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe um número inteiro: '))
n3 = float(input('Informe um número real: '))

a = (n1 * 2) * (n2 / 2)
b = (n1 * 3) + (n3 * 3)
c = n3 ** 3

print('O produto do dobro do primeiro com metade do segundo é: {}'.format(a))
print('A soma do triplo do primeiro com o terceiro é: {}'.format(b))
print('O terceiro elevado ao cubo: {:.2f}'.format(c))
