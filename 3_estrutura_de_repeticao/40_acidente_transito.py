"""
40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados
sobre acidentes de trânsito. Foram obtidos os seguintes dados:
    a. Código da cidade;
    b. Número de veículos de passeio (em 1999);
    c. Número de acidentes de trânsito com vítimas (em 1999).

    Deseja-se saber:
    d. Qual o maior e menor índice de acidentes de transito e a que cidade
    pertence;
    e. Qual a média de veículos nas cinco cidades juntas;
    f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000
    veículos de passeio.
"""

dados = []
count = 1
while count <= 5:
    codigo, veiculos, acidentes = input("Informe o código da cidade, o número "
                                        "de veículos de passeio e o número de "
                                        "acidentes com vítimas em 1999: ") \
        .split()
    codigo, veiculos, acidentes = int(codigo), int(veiculos), int(acidentes)
    dados.append({'Código': codigo, 'Veículos': veiculos,
                  'Acidentes': acidentes})
    count += 1

maior_acidentes = -1
menor_acidentes = 9999999
total_veiculos = 0
total_acidentes = 0
cidades_acidente = 0

for dado in dados:
    if dado['Acidentes'] > maior_acidentes:
        codigo_maior_indice = dado['Código']
        maior_acidentes = dado['Acidentes']
    if dado['Acidentes'] < menor_acidentes:
        codigo_menor_indice = dado['Código']
        menor_acidentes = dado['Acidentes']
    if dado['Veículos'] <= 2000:
        total_acidentes += dado['Acidentes']
        cidades_acidente += 1

    total_veiculos += dado['Veículos']

print("A cidade de número {} possui o índice de {} acidentes, sendo o maior."
      .format(codigo_maior_indice, maior_acidentes))
print("A cidade de número {} possui o índice de {} acidentes, sendo o menor."
      .format(codigo_menor_indice, menor_acidentes))
print("A média de veículos nas cinco cidades juntas é de {} veículos."
      .format(total_veiculos))
print("A média de acidentes de trânsito nas cidades com menos de 2.000 veículos"
      " de passeio é de {:.2f}.".format(total_acidentes / cidades_acidente))
