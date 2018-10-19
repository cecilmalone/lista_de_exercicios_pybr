"""
7. Faça um programa que leia 5 números e informe o maior número.
"""
n = 0

for x in range(5):
    numero = int(input("Informe um número: "))
    if numero > n:
        n = numero

print("O maior número é", n)
