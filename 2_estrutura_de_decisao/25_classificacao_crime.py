"""
25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As 
perguntas são:
    a. "Telefonou para a vítima?"
    b. "Esteve no local do crime?"
    c. "Mora perto da vítima?"
    d. "Devia para a vítima?"
    e. "Já trabalhou com a vítima?" 
    O programa deve no final emitir uma classificação sobre a participação da 
    pessoa no crime. 
    Se a pessoa responder positivamente a 2 questões ela deve ser classificada 
    como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso 
    contrário, ele será classificado como "Inocente".
"""

telefone = input("Telefonou para a vítima?")
local = input("Esteve no local do crime?")
mora_perto = input("Mora perto da vítima?")
devedor = input("Devia para a vítima?")
trabalho = input("Já trabalhou com a vítima?")

total_sim = 0

if telefone.lower() == "sim":
    total_sim += 1
elif local.lower() == "sim":
    total_sim += 1
elif mora_perto.lower() == "sim":
    total_sim += 1
elif devedor.lower() == "sim":
    total_sim += 1
elif trabalho.lower() == "sim":
    total_sim += 1

if total_sim == 2:
    print("A classificação desta pessoa é: Suspeita")
elif total_sim == 3 or total_sim == 4:
    print("A classificação desta pessoa é: Cúmplice")
elif total_sim == 5:
    print("A classificação desta pessoa é: Assassino")
else:
    print("A classificação desta pessoa é: Inocente")
