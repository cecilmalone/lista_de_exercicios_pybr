"""
22. Altere o programa de cálculo dos números primos, informando, caso o número 
não seja primo, por quais número ele é divisível.
"""

numero = int(input("Informe um número: "))

if (numero % numero == 0) and (numero % 1 == 0):
    print("O número {} é primo.".format(numero))
else:
    print("O número {} não é primo.".format(numero))
    nao_primos_divisao = []
    for n in range(numero):
        if numero % n == 0:
            nao_primos_divisao.append(n)
    print("Os números que dividem com {} são: {}".format(numero, nao_primos_divisao))
