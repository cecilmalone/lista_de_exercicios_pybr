"""
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
	a. salário bruto.
	b. quanto pagou ao INSS.
	c. quanto pagou ao sindicato.
	d. o salário líquido.
	e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
		+ Salário Bruto : R$
		- IR (11%) : R$
		- INSS (8%) : R$
		- Sindicato ( 5%) : R$
		= Salário Liquido : R$
		Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor_hora = float(input())
hora_mes = float(input())

salario_bruto = valor_hora * hora_mes
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
irpf = salario_bruto * 0.11
descontos = inss + sindicato + irpf
salario_liquido = salario_bruto - descontos


print('a:', salario_bruto)
print('b:', inss)
print('c:', sindicato)
print('d:', salario_bruto)
print(f'+ Salário Bruto : R$ {salario_bruto} \n- IR (11%) : R$ {irpf} \n - INSS (8%) : R$ {inss} \n- Sindicato ( 5%) : R$ {sindicato} \n= Salário Liquido : R$ {salario_liquido}'