"""
14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""

par = 0
impar = 0

for _ in range(1, 10):
    numero = int(input("Informe um número: "))

    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print("Números pares:", par)
print("Números ímpares:", impar)
