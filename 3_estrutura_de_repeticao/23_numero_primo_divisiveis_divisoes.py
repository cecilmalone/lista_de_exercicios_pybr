"""
23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número 
inteiro fornecido pelo usuário. O programa deverá mostrar também o número de 
divisões que ele executou para encontrar os números primos. Serão avaliados o 
funcionamento, o estilo e o número de testes (divisões) executados.
"""

numero = int(input("Informe um número: "))

divisiveis = [1]
divisoes = 0

for n in range(numero):
    if (n % n == 0) and (n % 1 == 0):
        divisiveis.append(n)
        divisoes += 1

print("O número {} possui os seguintes divisiveis: {}".format(numero, divisiveis))
print("O número {} possui {} divisões".format(divisoes))
