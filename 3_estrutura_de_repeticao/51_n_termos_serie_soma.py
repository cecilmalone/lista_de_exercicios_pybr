"""
51. Faça um programa que mostre os n termos da Série a seguir:
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
    Imprima no final a soma da série.
"""

n_termos = int(input("Informe a quantidade de termos: "))

numerador = 1
denominador = 1

lista_valores = [1]

print("S = ")

for x in range(n_termos):
    if x == n_termos:
	    print(numerador + "/" + denominador + ".", end='')
	else:
	    print(numerador + "/" + denominador + " + ", end='')
	
	lista_valores.append(numerador/denominador)
    
	numerador += 1
	denominador += 2
	
print("Valor de S: {}".format(sum(lista_valores)))