"""
31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
agora possui uma loja de conveniências. Faça um programa que implemente uma
caixa registradora rudimentar. O programa deverá receber um número desconhecido
de valores referentes aos preços das mercadorias. Um valor zero deve ser
informado pelo operador para indicar o final da compra. O programa deve então
mostrar o total da compra e perguntar o valor em dinheiro que o cliente
forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o
programa deverá voltar ao ponto inicial, para registrar a próxima compra. A
saída deve ser conforme o exemplo abaixo:
    Lojas Tabajara
    Produto 1: R$ 3.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00
    ...
"""

while True:
    valores = []
    total = 0.0

    while 0.0 not in valores:
        valor = float(input("Informe o valor da mercadoria: "))
        valores.append(valor)

    print("Lojas Tabajara")
    for valor in valores:
        x = 0
        print("Produto {}: R$ {:.2f}".format(x+1, valor))
        total += valor
        x += 1

    print("Total: R$ {:.2f}".format(total))

    dinheiro = float(input("Valor em Dinheiro: "))
    troco = dinheiro - total

    print("Troco: R$ {:.2f}".format(troco))
    print("...")
