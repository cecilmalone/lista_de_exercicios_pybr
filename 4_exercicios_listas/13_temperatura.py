"""
13. Faça um programa que receba a temperatura média de cada mês do ano e 
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e 
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

meses = {'1 - Janeiro': 0, "2 - Fevereiro": 0, "3 - Março": 0, "4 - Abril": 0, "5 - Maio": 0,
		"6 - Junho": 0, "7 - Julho": 0, "8 - Agosto": 0, "9 - Setembro": 0, "10 - Outubro": 0,
		"11 - Novembro": 0, "12 - Dezembro": 0}
media = 0

for x in range(12):
    temperatura = float(input("Informe a temperatura de {}: ".format(meses[x]))
    meses[x] = temperatura 

media = media / len(meses)

for x in meses:
	if meses[x][1] > media:
		print("{}: {}".format(meses[x][0], meses[x][1]))
