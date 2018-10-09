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

valor_hora = float(input('Informe o valor da hora trabalhada: '))
hora_mes = float(input('Informe a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora * hora_mes
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
irpf = salario_bruto * 0.11
descontos = inss + sindicato + irpf
salario_liquido = salario_bruto - descontos

print('Salário Bruto: R$ %.2f' % salario_bruto)
print('INSS: R$ %.2f' % inss)
print('Sindicato: R$ %.2f' % sindicato)
print('Salário Líquido: R$ %.2f' % salario_liquido)

print('+ Salário Bruto: R$ %.2f' % salario_bruto)
print('- IR (11%%): R$ %.2f' % irpf)
print('- INSS (8%%): R$ %.2f' % inss)
print('- Sindicato ( 5%%) : R$ %.2f' % sindicato)
print('= Salário Liquido : R$ %.2f' % salario_liquido)
