"""
15. Faça um programa que leia um número indeterminado de valores, 
correspondentes a notas, encerrando a entrada de dados quando for 
informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
    a. Mostre a quantidade de valores que foram lidos;
    b. Exiba todos os valores na ordem em que foram informados, um ao lado do 
	outro;
    c. Exiba todos os valores na ordem inversa à que foram informados, um 
	abaixo do outro;
    d. Calcule e mostre a soma dos valores;
    e. Calcule e mostre a média dos valores;
    f. Calcule e mostre a quantidade de valores acima da média calculada;
    g. Calcule e mostre a quantidade de valores abaixo de sete;
    h. Encerre o programa com uma mensagem;
"""

valores = []
count = 0
soma = 0

while True:
    valor = float(input("Informe um número: "))
    if valor == -1:
        break
    else:
        valores.append(valor)
        count += 1

for x in range(len(valores)):
    soma += x

media = soma / len(valores)
acima_media = [sum(x) for x in valores if x > media]
abaixo_sete = [sum(x) for x in valores if x < 7]


print("a. Foram lidos {} números".format(count))
print("b. Os valores na ordem foram: {}".format(valores))
print("c. Os valores invertidos foram: {}".format(valores[::-1]))
print("d. Os valores somados é igual a {}.".format(soma))
print("e. A média é igual a {}.".format(media))
print("f. {} números são maiores que a média.".format(acima_media))
print("g. {} números são menores do que 7.".format(abaixo_sete))
print("O programa foi finalizado!")
