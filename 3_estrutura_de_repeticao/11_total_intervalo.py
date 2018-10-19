"""
11. Altere o programa anterior para mostrar no final a soma dos números.
"""

n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))

total = 0

for x in range(n1+1, n2-1):
    total += x
    print(x)

print("Total:", total)
