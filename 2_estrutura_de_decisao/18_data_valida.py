"""
18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a 
mesma é uma data válida.
"""

data = input("Informe uma data no formato dd/mm/aaaa: ")


if (int(data[3:4]) == 2) and (int(data[0:1]) > 29) and ((int(data[6:9]) % 4 == 0) and (int(data[6:9]) % 100 != 0) and (int(data[6:9]) % 400 != 0)):
    print("Data inválida")
elif (int(data[3:4]) == 2) and (int(data[0:1]) > 28):
    print("Data inválida")
elif (int(data[0:1]) < 1) and (int(data[0:1]) > 31):
    print("Data inválida")
elif (int(data[3:4]) < 1) and (int(data[:1]) > 12):
    print("Data inválida")
elif int(data[6:9]) < 1900:
    print("Data inválida")
else:
    print("Data válida")