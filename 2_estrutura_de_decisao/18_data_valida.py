"""
18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a 
mesma é uma data válida.
"""

data = input("Informe uma data no formato dd/mm/aaaa: ")


if (int(data[3:5]) == 2) and (int(data[0:2]) > 29) and ((int(data[6:10]) % 4 == 0) and (int(data[6:10]) % 100 != 0) and (int(data[6:10]) % 400 != 0)):
    print("Data inválida")
elif (int(data[3:5]) == 2) and (int(data[0:2]) > 28):
    print("Data inválida")
elif (int(data[0:2]) < 1) and (int(data[0:2]) > 31):
    print("Data inválida")
elif (int(data[3:5]) < 1) and (int(data[:2]) > 12):
    print("Data inválida")
elif int(data[6:10]) < 1900:
    print("Data inválida")
else:
    print("Data válida")
