"""
20. Faça um Programa para leitura de três notas parciais de um aluno. O programa 
deve calcular a média alcançada por aluno e presentar:
    a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva 
    média alcançada;
    b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva 
    média alcançada;
    c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

nota_1 = float(input("Informe uma nota: "))
nota_2 = float(input("Informe uma nota: "))
nota_3 = float(input("Informe uma nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if (media >= 0) and (media < 7):
    print("Reprovado, com a média {}".format(media))
elif (media >= 7) and (media < 10):
    print("Aprovado, com a média {}".format(media))
else:
    print("Aprovado com Distinção, com a média {}".format(media))
