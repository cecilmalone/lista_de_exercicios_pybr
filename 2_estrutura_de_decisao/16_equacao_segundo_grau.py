"""
16. Faça um programa que calcule as raízes de uma equação do segundo grau, na 
forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as 
consistências, informando ao usuário nas seguintes situações:
    a. Se o usuário informar o valor de A igual a zero, a equação não é do 
    segundo grau e o programa não deve fazer pedir os demais valores, sendo 
    encerrado;
    b. Se o delta calculado for negativo, a equação não possui raizes reais. 
    Informe ao usuário e encerre o programa;
    c. Se o delta calculado for igual a zero a equação possui apenas uma raiz 
    real; informe-a ao usuário;
    d. Se o delta for positivo, a equação possui duas raiz reais; informe-as 
    ao usuário;
"""
import sys

a = int(input("Informe o a: "))

if a == 0:
    sys.exit(0)

b = int(input("Informe o b: "))
c = int(input("Informe o c: "))

delta = (b ** 2) - 4 * (a * c)

if delta < 0:
    print("A equação não posui raizes reais.")
    sys.exit(0)
elif delta == 0:
    print("A equação possui apenas uma raiz real")
    x = -b / (2 * a)
    print ("X' = X'' = {}".format(x))
elif delta > 0:
    print("A equação possui duas raiz reais")
    x_1 = (-b + delta) / (2 * a)
    x_2 = (-b - delta) / (2 * a)
    print ("X' = {}".format(x_1))
    print ("X'' = {}".format(x_2))
