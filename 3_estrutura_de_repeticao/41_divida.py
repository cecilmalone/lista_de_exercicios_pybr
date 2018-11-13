"""
41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
 seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e
 valor da parcela.
    Os juros e a quantidade de parcelas seguem a tabela abaixo:
    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25
    Exemplo de saída do programa:
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67
"""

import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

valor_divida = float(input("Informe o valor da dívida (em reais): "))
parcelas_juros = [[1, 0], [3, 10], [6, 15], [9, 20], [12, 25]]

print("Valor da Dívida  Valor dos Juros Quantidade de Parcelas  "
      "Valor da Parcela")

for parcela, juros in parcelas_juros:
    valor_juros = valor_divida * (juros / 100)
    divida_com_juros = valor_divida + valor_juros
    parcelamento = divida_com_juros / parcela
    print("R$ {}        {}              {:d}                    "
          "R$ {}".format(locale.format("%.2f", divida_com_juros,
                                       grouping=True),
                         locale.format("%.2f", valor_juros,
                                       grouping=True),
                         parcela,
                         locale.format("%.2f", parcelamento,
                                       grouping=True)))
