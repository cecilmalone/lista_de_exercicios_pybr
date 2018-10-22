"""
26. Numa eleição existem três candidatos. Faça um programa que peça o número 
total de eleitores. Peça para cada eleitor votar e ao final mostrar o número 
de votos de cada candidato.
"""

total_eleitores = int(input("Informe a quantidade de eleitores: "))

votos = []
cand_1 = 0
cand_2 = 0
cand_3 = 0

for x in range(total_eleitores):
    voto = int(input("Eleitor nº {}, informe o seu voto: ".format(x+1)))
    votos.append(voto)

for item in votos:
    if item == 1:
        cand_1 += 1
    elif item == 2:
        cand_2 += 1
    elif item == 3:
        cand_3 += 1

print("O candidato nº 1 teve {} voto(s).".format(cand_1))
print("O candidato nº 2 teve {} voto(s).".format(cand_2))
print("O candidato nº 3 teve {} voto(s).".format(cand_3))
