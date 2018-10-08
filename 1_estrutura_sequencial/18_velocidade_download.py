"""
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
aproximado de download do arquivo usando este link (em minutos).
"""

mb_arquivo = float(input())
mbps_link = float(input())

velocidade_segundos = mb_arquivo / mbps_link
velocidade_minutos = velocidade_segundos / 60

print(velocidade_minutos)

