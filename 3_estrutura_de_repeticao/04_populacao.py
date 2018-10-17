"""
4. Supondo que a população de um país A seja da ordem de 80000 habitantes com 
uma taxa anual de crescimento de 3% e que a população de B seja 200000 
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
e escreva o número de anos necessários para que a população do país A 
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

pop_a = 80000
tax_a = 0.03
pop_b = 200000
tax_b = 0.015
anos = 0

while pop_a <= pop_b:
    pop_a += (pop_a * tax_a)
    pop_b += (pop_b * tax_b)
    anos += 1

print("A população A ultrapassará ou igualará a população B em {} anos.".format(anos))
