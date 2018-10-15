"""
19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a 
quantidade de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros. 
    Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades 
    Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 
    21, 11, 1, 7 e 16
"""

numero = float(input("Informe um número: "))

while numero >= 1000:
    numero = float(input("Informe um número: "))

texto = str(numero)

if len(numero) == 3:
    if int(texto[0]) > 1:
        centena = "{} centenas,".format(texto[0])
    else:
        centena = "{} centena,".format(texto[0])
elif len(numero) == 2:
    if int(texto[1]) > 1:
        dezena = "{} dezenas,".format(texto[1])
    else:
        dezena = "{} dezena,".format(texto[1])
else:
    if int(texto[2]) > 1:
        unidade = "{} unidades".format(texto[2])
    else:
        unidade = "{} unidade".format(texto[2])

if len(numero) == 3:
    print(centena + dezena + unidade)
elif len(numero) == 2:
    print(dezena + unidade)
else:
    print(unidade)
    
