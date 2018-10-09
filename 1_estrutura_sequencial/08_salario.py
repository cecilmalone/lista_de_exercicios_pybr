"""
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

valor_hora = float(input('Quanto você ganha por hora: '))
horas_trabalhadas_mes = int(input('Quantas horas foram trabalhadas no mês: '))

salario = valor_hora * horas_trabalhadas_mes

print('O total do salário é de: R$ {:.2f}'.format(salario))
