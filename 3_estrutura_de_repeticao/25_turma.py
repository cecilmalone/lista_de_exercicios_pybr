"""
25. Faça um programa que peça para n pessoas a sua idade, ao final o programa 
devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e 
maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a 
média calculada.
"""

idades = []
idades.append(int(input("Informe a idade: "))

while idade <> 0:
    idades.append(int(input("Informe a idade: "))

idades = [int(x) for x in idades]

soma = 0

for n in idades:
    soma += n

media = soma / len(idades)

if (media > 0) and (media <= 25):
    print("Esta turma é jovem.")
elif (media >= 26) and (media <= 60):
    print("Esta turma é adulta.")
elif media > 60:
    print("Esta turma é idosa.")
