"""
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus 
colaboradores e lhe contraram para desenvolver o programa que calculará os 
reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste 
    segundo o seguinte critério, baseado no salário atual:
        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser 
        realizado, informe na tela:
        
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
"""

salario_atual = float(input("Informe o salário atual: "))

if salario_atual <= 280:
    percentual = 20
    novo_salario = salario_atual + (salario_atual * 0.20)
elif (salario_atual > 280) and (salario_atual <= 700):
    percentual = 15
    novo_salario = salario_atual + (salario_atual * 0.15)
elif (salario_atual > 700) and (salario_atual <= 1500):
    percentual = 10
    novo_salario = salario_atual + (salario_atual * 0.10)
else:
    percentual = 5
    novo_salario = salario_atual + (salario_atual * 0.05)

print("Salário antes do reajuste: R$ {:.2f}".format(salario_atual))
print("Percentual de aumento aplicado: {}%".format(percentual))
print("O valor do aumento: R$ {:.2f}".format(novo_salario - salario_atual))
print("Novo salário: R$ {:.2f}".format(novo_salario))
