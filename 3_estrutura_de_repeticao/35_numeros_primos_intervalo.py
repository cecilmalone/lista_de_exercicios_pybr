"""
35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma
 lista dos números primos existentes entre 1 e um número inteiro informado pelo
 usuário.
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