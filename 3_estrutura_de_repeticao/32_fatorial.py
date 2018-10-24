"""
32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120
"""

numero = int(input("Informe um número: "))

fatorial = 1

print("Fatorial de: {}".format(numero))
print("{}! = ".format(numero), end='')

while numero > 0:
    fatorial = fatorial * numero
    if numero == 1:
        print(numero, end='')
    else:
        print(numero, end=' . ')
    numero -= 1

print(" = {}".format(fatorial))
