"""
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input()

if letra in (a, e, i, o, u):
    print("A letra %s é uma vogal" % letra)
else:
    print("A letra {} é uma consoante".format(letra))
