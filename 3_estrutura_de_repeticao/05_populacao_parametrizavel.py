"""
5. Altere o programa anterior permitindo ao usuário informar as populações e as 
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""
while True:
    pop_a = int(input("Informe a população de A: "))
    tax_a = float(input("Informe a taxa de crescimento da população A: "))
    pop_b = int(input("Informe a população de B: "))
    tax_b = float(input("Informe a taxa de crescimento da população B: "))
    anos = 0

    while pop_a <= pop_b:
        pop_a += (pop_a * tax_a)
        pop_b += (pop_b * tax_b)
        anos += 1

    print("A população A ultrapassará ou igualará a população B em {} anos.".format(anos))
    repetir = input("Deseja repetir a operação: ")
    if repetir.lower() == 's' or repetir.lower() == 'sim':
        continue
    else:
        break
