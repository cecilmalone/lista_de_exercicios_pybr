"""
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar 
M-Matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem "Bom Dia!", "Boa 
Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

turno = input("Qual o turno que você estuda: ")

if turno == 'M' or turno == "Matutino":
    print("Bom Dia!")
elif turno == 'V' or turno == "Vespertino":
    print("Boa Tarde!")
elif turno == 'N' or turno == "Noite":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
