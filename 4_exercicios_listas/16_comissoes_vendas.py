"""
16. Utilize uma lista para resolver o problema a seguir. 
Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 
por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe 
$200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa 
(usando um array de contadores) que determine quantos vendedores receberam 
salários nos seguintes intervalos de valores:
    a. $200 - $299
    b. $300 - $399
    c. $400 - $499
    d. $500 - $599
    e. $600 - $699
    f. $700 - $799
    g. $800 - $899
    h. $900 - $999
    i. $1000 em diante
    Desafio: Crie ma fórmula para chegar na posição da lista a partir do 
    salário, sem fazer vários ifs aninhados.
"""

salarios = []

print("a. $200 - $299: {}".format([salarios.count(x) for x in range(200, 300)]))
print("b. $300 - $399: {}".format([salarios.count(x) for x in range(300, 400)]))
print("c. $400 - $499: {}".format([salarios.count(x) for x in range(400, 500)]))
print("d. $500 - $599: {}".format([salarios.count(x) for x in range(500, 600)]))
print("e. $600 - $699: {}".format([salarios.count(x) for x in range(600, 700)]))
print("f. $700 - $799: {}".format([salarios.count(x) for x in range(700, 800)]))
print("g. $800 - $899: {}".format([salarios.count(x) for x in range(800, 900)]))
print("h. $900 - $999: {}".format([salarios.count(x) for x in range(900, 1000)]))
print("i. $1000 em diante: {}".format([salarios.count(x) for x in range(1000, 9999)]))
