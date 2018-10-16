"""
12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os 
descontos são do Imposto de Renda, que depende do salário bruto (conforme 
tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário 
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido 
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao 
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% 
    Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.
            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00  
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
"""

valor_hora = float(input("Informe o valor da hora trabalhada: "))
qtd_horas_mes = float(input("Informe a quantidad de horas trabalhadas no mês: "))
salario_bruto = valor_hora * qtd_horas_mes

if salario_bruto <= 900:
    ir = 'isento'
    irpf = 0
elif (salario_bruto > 900) and (salario_bruto <= 1500):
    ir = '5'
    irpf = salario_bruto * 0.05
elif (salario_bruto > 1500) and (salario_bruto <= 2500):
    ir = '10'
    irpf = salario_bruto * 0.10
else:
    ir = '20'
    irpf = salario_bruto * 0.20

fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03
inss = salario_bruto * 0.10

descontos = irpf + inss + sindicato
salario_liquido = salario_bruto - descontos

print("Salário Bruto: ({} * {})        : R$ {:.2f}".format(valor_hora, qtd_horas_mes, salario_bruto))
print("(-) IR ({}%)                    : R$ {:.2f}".format(ir, irpf))
print("(-) INSS ( 10%)                 : R$  {:.2f}".format(inss))
print("FGTS (11%)                      : R$  {:.2f}".format(fgts))
print("Total de descontos              : R$  {:.2f}".format(descontos))
print("Salário Liquido                 : R$  {:.2f}".format(salario_liquido))
