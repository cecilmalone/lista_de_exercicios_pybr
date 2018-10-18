"""
28. Faça um programa que calcule o valor total investido por um colecionador em 
sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá 
informar a quantidade de CDs e o valor para em cada um.
"""

valor_total = 0
valor_medio = 0
valores_cds = []

qtd_cds = int(input("Informe a quantidade de CD's da coleção: "))

for n in range(qtd_cds):
    valor_cd = float(input("Informe o valor do CD nº {}".format(n)))
    valores_cds.append(valor_cd)

for valor in valores_cds:
    valor_total += valor

valor_medio = valor_total / qtd_cds

print("O valor total da coleção de CD's é de R$ {:.2f}".format(valor_total))
print("O valor médio gasto na coleção de CD's foi de R$ {:.2f}".format(valor_medio))
