"""
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
aproximado de download do arquivo usando este link (em minutos).
"""

mb_arquivo = float(input('Informe o tamanho de um arquivo para download (em MB): '))
mbps_link = float(input('Informe a velocidade do link de Internet (em Mbps): '))

velocidade_segundos = mb_arquivo / mbps_link
velocidade_minutos = velocidade_segundos / 60

print('O tempo aproximado para download do arquivo é de %d minuto(s).' %velocidade_minutos)

