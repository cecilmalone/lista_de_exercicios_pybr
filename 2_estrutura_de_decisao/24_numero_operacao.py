"""
24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual 
operação ele deseja realizar. O resultado da operação deve ser acompanhado de 
uma frase que diga se o número é:
    a. par ou ímpar;
    b. positivo ou negativo;
    c. inteiro ou decimal.
"""

n1 = float(input("Informe um número: "))
n2 = float(input("Informe outro número: "))
operacao = input("Informe qual operação deseja realizar: ")

if operacao == "+" or operacao.lower() == "soma":
    resultado = n1 + n2
elif operacao == "-" or operacao.lower() == "subtração":
    resultado = n1 - n2
if operacao == "*" or operacao.lower() == "multiplicação":
    resultado = n1 * n2
if operacao == "/" or operacao.lower() == "divisão":
    resultado = n1 / n2

print("O resultado da operação é igual a {}".format(resultado))

if resultado % 2 == 0:
    print("O resultado é par.")
else:
    print("O resultado é ímpar.")

if resultado >= 0:
    print("O resultado é positivo.")
else:
    print("O resultado é negativo.")

if round(resultado) != resultado:
    print("O resultado é decimal.")
else:
    print("O resultado é inteiro.")
