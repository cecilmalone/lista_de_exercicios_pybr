"""
42. Faça um programa que leia uma quantidade indeterminada de números positivos
e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e
 [76-100]. A entrada de dados deverá terminar quando for lido um número
 negativo.
"""
zero_vinte_cinco = 0
vinte_seis_cinquenta = 0
cinquenta_um_setenta_cinco = 0
setenta_seis_cem = 0
numero = 999

while numero >= 0:
    numero = int(input("Informe um número: "))

    if 0 <= numero <= 25:
        zero_vinte_cinco += 1
    elif 26 <= numero <= 50:
        vinte_seis_cinquenta += 1
    elif 51 <= numero <= 75:
        cinquenta_um_setenta_cinco += 1
    elif 76 <= numero <= 100:
        setenta_seis_cem += 1

print("Quantidade números entre 0 e 25:", zero_vinte_cinco)
print("Quantidade números entre 26 e 50:", vinte_seis_cinquenta)
print("Quantidade números entre 51 e 75:", cinquenta_um_setenta_cinco)
print("Quantidade números entre 76 e 100:", setenta_seis_cem)
