"""
12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""

altura = float(input('Informe a altura: '))

peso_ideal = (72.7 * altura) - 58

print('O peso ideal para a altura de {} é: {:.2f} kg'.format(altura, peso_ideal))
