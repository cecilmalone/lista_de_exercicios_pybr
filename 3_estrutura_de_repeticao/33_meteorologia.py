"""
33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas, e informe ao
final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.
"""

temperaturas = []

temperaturas = input("Informe as temperaturas: ").split()
temperaturas = [float(x) for x in temperaturas]

maior = max(temperaturas)
menor = min(temperaturas)
media = 0
total = 0

for temp in temperaturas:
    total += temp

media = total / len(temperaturas)

print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
print("Temperatura média:", media)
