"""
19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

numeros = []

numeros = input("Informe um conjunto de números: ").split()

if (numeros < 0) or numeros > 1000:
    numeros = input("Informe um conjunto de números: ").split()

maior = max(numeros)
menor = min(numeros)

for x in numeros:
    soma =+ x

print("Maior valor:", maior)
print("Menor valor:", menor)
print("Soma dos valores:", soma)