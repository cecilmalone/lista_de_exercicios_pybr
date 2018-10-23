"""
23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número 
inteiro fornecido pelo usuário. O programa deverá mostrar também o número de 
divisões que ele executou para encontrar os números primos. Serão avaliados o 
funcionamento, o estilo e o número de testes (divisões) executados.
"""

numero = int(input("Informe um número: "))

tot = 0
div = 0

for j in range(1, numero + 1):
    tot = 0
    div = 0
    for c in range(1, numero + 1):
        if j % c == 0:
            tot += 1
            if tot <= 2:
                div += 1

    if tot == 2:
        print("O número {} é primo e teve {} divisões até ser encontrado."
              .format(j, div))
