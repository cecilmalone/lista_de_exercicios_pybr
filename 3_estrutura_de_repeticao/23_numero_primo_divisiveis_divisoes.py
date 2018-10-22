"""
23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número 
inteiro fornecido pelo usuário. O programa deverá mostrar também o número de 
divisões que ele executou para encontrar os números primos. Serão avaliados o 
funcionamento, o estilo e o número de testes (divisões) executados.
"""

numero = int(input("Informe um número: "))

divisiveis = [1]
divisoes = 0

for n in range(1, numero):
    if (n % n == 0) and (n % 1 == 0):
        divisiveis.append(n)
        divisoes += 1

print("O número {} possui os seguintes divisiveis: {}".format(numero, divisiveis))
print("O número {} possui {} divisões".format(divisoes))


numero = int(input("Informe um número: "))
tot = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        tot += 1

if tot == 2:
    print("O número {} é primo.".format(numero))
else:
    print("O número {} não é primo.".format(numero))

