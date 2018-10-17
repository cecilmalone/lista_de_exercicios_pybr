"""
20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o 
fatorial várias vezes e limitando o fatorial a números inteiros positivos e 
menores que 16.
"""

while True:
    numero = int(input("Informe um número: "))

    while (numero < 0) or (numero > 16):
        numero = int(input("Informe um número: "))

    resultado = 1
    lista = []

    for x in range(numero):
        resultado *= x
        lista.append(resultado)

    for y in range(len(lista)):
        print("{}!={}={}".format(numero, lista[::-1], resultado))
