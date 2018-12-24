"""
17. Em uma competição de salto em distância cada atleta tem direito a cinco 
saltos. O resultado do atleta será determinado pela média dos cinco valores 
restantes. Você deve fazer um programa que receba o nome e as cinco distâncias 
alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a 
média dos saltos. O programa deve ser encerrado quando não for informado o 
nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
    Atleta: Rodrigo Curvêllo
    
    Primeiro Salto: 6.5 m
    Segundo Salto: 6.1 m
    Terceiro Salto: 6.2 m
    Quarto Salto: 5.4 m
    Quinto Salto: 5.3 m

    Resultado final:
    Atleta: Rodrigo Curvêllo
    Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
    Média dos saltos: 5.9 m
"""

while True:
    saltos = []
    atleta = input("Informe o nome do atleta: ")
    if atleta is null or atleta == '':
        break
    count = 1
    while count <= 5:
        salto = float("Informe o valor do {}º salto: ".format(count))
        saltos.append(salto)

    
    print("Atleta: {}".format(atleta))
    print()
    print("Primeiro Salto: {} m".format(saltos[0]))
    print("Segundo Salto: {} m".format(saltos[1]))
    print("Terceiro Salto: {} m".format(saltos[2]))
    print("Quarto Salto: {} m".format(saltos[3]))
    print("Quinto Salto: {} m".format(saltos[4]))
    print()
    print("Resultado final:")
    print("Atleta: {}".format(atleta))
    print("Saltos: {} - {} - {} - {} - {}"format(saltos[0], saltos[1], saltos[2],
                                                saltos[3], saltos[4]))
    print("Média dos saltos: {} m".format(sum(saltos) / 5))
