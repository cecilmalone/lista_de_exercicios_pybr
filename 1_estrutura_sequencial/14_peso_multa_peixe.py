"""
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um 
programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na 
variável excesso a quantidade de quilos além do limite e na variável multa o valor 
da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

valor_multa = 4.00
peso = float(input('Informe o peso dos peixes: '))

if peso > 50:
    quantidade_excesso = peso - 50
    multa = quantidade_excesso * valor_multa
    print('A quantidade de excesso de peixe foi de: {} kg'.format(quantidade_excesso))
    print('A multa a ser paga pelo excesso de peixe é de: R$ {:.2f}'.format(multa))
else:
    print('A quantidade de peixe foi de: {} kg'.format(peso))
