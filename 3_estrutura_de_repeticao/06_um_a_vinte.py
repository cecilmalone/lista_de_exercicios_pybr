"""
6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""
resultado = ''

for x in range(1, 20):
    print(x)

for x in range(1, 20):
    resultado = resultado + str(x) + ' '

print(resultado)