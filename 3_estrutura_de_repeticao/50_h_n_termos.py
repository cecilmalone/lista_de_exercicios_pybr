"""
50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o 
valor de H com N termos.
"""

n_termos = int(input("Informe a quantidade de termos: "))

numerador = 1
denominador = 2

lista_valores = [1]

print("H = ")

for x in range(n_termos):
    if x == n_termos:
	    print(numerador + "/" + denominador + ".", end='')
	else:
	    print(numerador + "/" + denominador + " + ", end='')
	
	lista_valores.append(numerador/denominador)
	
	denominador += 1
	
print("Valor de H: {}".format(sum(lista_valores)))
    