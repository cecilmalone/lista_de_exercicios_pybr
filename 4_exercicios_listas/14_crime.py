"""
14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa 
sobre um crime. As perguntas são:
    a. "Telefonou para a vítima?"
    b. "Esteve no local do crime?"
    c. "Mora perto da vítima?"
    d. "Devia para a vítima?"
    e. "Já trabalhou com a vítima?" 
    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
	Se a pessoa responder positivamente a 2 questões ela deve ser classificada 
	como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
	Caso contrário, ele será classificado como "Inocente".
"""
respostas = []

question_a = input("Telefonou para a vítima?")
if question_a.lower() in ('sim', 's'):
	respostas.append(True)
question_b = input("Esteve no local do crime?")
if question_b.lower() in ('sim', 's'):
	respostas.append(True)
question_c = input("Mora perto da vítima?")
if question_c.lower() in ('sim', 's'):
	respostas.append(question_a)
question_d = input("Devia para a vítima?")
if question_d.lower() in ('sim', 's'):
	respostas.append(question_a)
question_e = input("Já trabalhou com a vítima?")
if question_e.lower() in ('sim', 's'):
	respostas.append(question_a)

if sum(respostas) == 5:
	print("Classificação: Assassino")
elif sum(respostas) == 4 or sum(respostas) == 3:
	print("Classificação: Cúmplice")
elif sum(respostas) == 2:
	print("Classificação: Suspeita")
if sum(respostas) <= 1:
	print("Classificação: Inocente")
