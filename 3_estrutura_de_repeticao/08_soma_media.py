"""
8. Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

for _ in range(1, 5):
    numero = int(input("Informe um número: "))
    resultado += numero

print("A soma dos números é igual a", resultado)
print("A média dos números é igual a", resultado / 5)
