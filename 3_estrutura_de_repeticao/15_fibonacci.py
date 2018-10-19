"""
15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
"""
n = int(input("Informe a quantidade de termos: "))

t1 = 0
t2 = 1
count = 3

if n == 1:
    print("{}".format(t2))

while count <= n:
    t3 = t1 + t2
    print("{}".format(t3), end=' ')
    t1 = t2
    t2 = t3
    count += 1
