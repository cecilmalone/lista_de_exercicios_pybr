"""
46. Em uma competição de salto em distância cada atleta tem direito a cinco 
saltos. No final da série de saltos de cada atleta, o melhor e o pior 
resultados são eliminados. O seu resultado fica sendo a média dos três 
valores restantes. Você deve fazer um programa que receba o nome e as cinco 
distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos 
saltos conforme a descrição acima informada (retirar o melhor e o pior salto e 
depois calcular a média). Faça uso de uma lista para armazenar os saltos. 
Os saltos são informados na ordem da execução, portanto não são ordenados. 
O programa deve ser encerrado quando não for informado o nome do atleta. 
A saída do programa deve ser conforme o exemplo abaixo
    Atleta Rodrigo Curvêllo

    Primeiro Salto 6.5 m
    Segundo Salto 6.1 m
    Terceiro Salto 6.2 m
    Quarto Salto 5.4 m
    Quinto Salto 5.3 m

    Melhor salto  6.5 m
    Pior salto 5.3 m
    Média dos demais saltos 5.9 m

    Resultado final
    Rodrigo Curvêllo 5.9 m
"""

valor_saltos = 0
lista_saltos = []


while nome != "":
	nome = input("Informe o nome do atleta: ")
	dados = input("Informe a nota dos saltos: ").split()
	lista_saltos.append({'Nome': nome, 'Saltos': [float(x) for x in lista_saltos]})
	
melhor = max(lista_saltos['Saltos'])
pior = min(lista_saltos['Saltos'])

lista_saltos.remove(melhor)
lista_saltos.remove(pior)

for x in lista_saltos['Saltos']:
    valor_saltos += x

media = valor_saltos / 3

print(nome)
print()
print("Primeiro Salto {:.f} m".format(lista_saltos['Saltos'][0]))
print("Segundo Salto {:.f} m".format(lista_saltos['Saltos'][1]))
print("Terceiro Salto {:.f} m".format(lista_saltos['Saltos'][2]))
print("Quarto Salto {:.f} m".format(lista_saltos['Saltos'][3]))
print("Quinto Salto {:.f} m".format(lista_saltos['Saltos'][4]))
print()
print("Melhor salto {:.f} m".format(melhor))
print("Pior salto {:.f} m".format(pior))
print("Média dos demais saltos {:.f} m".format(media))
print()
print("Resultado final")
print("{} {:.f} m".format(nome, media))
