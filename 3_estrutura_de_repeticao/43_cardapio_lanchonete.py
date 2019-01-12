"""
43. O cardápio de uma lanchonete é o seguinte:
    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00
    Faça um programa que leia o código dos itens pedidos e as quantidades
    desejadas.
    Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total
    geral do pedido.
    Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

cardapio = [{'especificacao': 'Cachorro Quente', 'codigo': 100, 'valor': 1.20},
            {'especificacao': 'Bauru Simples', 'codigo': 101, 'valor': 1.30},
            {'especificacao': 'Bauru com ovo', 'codigo': 102, 'valor': 1.50},
            {'especificacao': 'Hambúrguer', 'codigo': 103, 'valor': 1.20},
            {'especificacao': 'Cheeseburguer', 'codigo': 104, 'valor': 1.30},
            {'especificacao': 'Refrigerante', 'codigo': 105, 'valor': 1.00}]

itens = []
codigo = 1

while codigo != 0:
    codigo = int(input("Informe o código do produto: "))
    quantidade = int(input("Informe a quantidade do produto: "))

    itens.append({'codigo': codigo, 'quantidade': quantidade})

print("Especificação        Quantidade      Preço")

for item in itens:
    print("{}        {}      {}".format(cardapio['espeficacao'],
                                        item['quantidade'],
                                        item['quantidade'] * cardapio['valor']))


