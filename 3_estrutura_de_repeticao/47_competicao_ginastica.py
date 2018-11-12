"""
47. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos 
votos restantes. Você deve fazer um programa que receba o nome do ginasta e 
as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois 
informe a sua média, conforme a descrição acima informada (retirar o melhor e 
o pior salto e depois calcular a média com as notas restantes). As notas não 
são informados ordenadas. Um exemplo de saída do programa deve ser conforme o 
exemplo abaixo:
    Atleta: Aparecido Parente
    Nota: 9.9
    Nota: 7.5
    Nota: 9.5
    Nota: 8.5
    Nota: 9.0
    Nota: 8.5
    Nota: 9.7

    Resultado final:
    Atleta: Aparecido Parente
    Melhor nota: 9.9
    Pior nota: 7.5
    Média: 9,04
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

print("Atleta:", nome)
print("Nota: {:.f}".format(lista_saltos['Saltos'][0]))
print("Nota: {:.f}".format(lista_saltos['Saltos'][1]))
print("Nota: {:.f}".format(lista_saltos['Saltos'][2]))
print("Nota: {:.f}".format(lista_saltos['Saltos'][3]))
print("Nota: {:.f}".format(lista_saltos['Saltos'][4]))
print("Nota: {:.f}".format(lista_saltos['Saltos'][5]))
print("Nota: {:.f}".format(lista_saltos['Saltos'][6]))
print()
print("Resultado final:")
print("Atleta:", nome)
print("Melhor nota: {:.f}".format(melhor))
print("Pior nota: {:.f}".format(pior))
print("Média: {:.f}".format(media))
