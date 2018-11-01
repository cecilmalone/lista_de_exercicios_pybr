"""
37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais
 alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um
 programa que pergunte a cada um dos clientes da academia seu código, sua altura
  e seu peso.
  O final da digitação de dados deve ser dada quando o usuário
  digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser
  informados os códigos e valores do clente mais alto, do mais baixo, do mais
  gordo e do mais magro, além da média das alturas e dos pesos dos clientes.
"""

clientes = []
codigo = 1
while codigo:
    codigo = int(input("Informe o codigo do cliente ou 0 para terminar: "))
    if codigo:
        altura = float(input("Informe a altura (em metros): "))
        peso = float(input("Informe o peso (em quilos): "))
        clientes.append({'Código': codigo, 'Altura': altura, 'Peso': peso})

mais_alto = -1
mais_baixo = 999
mais_gordo = -1
mais_magro = 999
total_altura = 0
total_peso = 0

for cliente in clientes:
    if cliente['Altura'] > mais_alto:
        codigo_mais_alto = cliente['Código']
        mais_alto = cliente['Altura']
    if cliente['Altura'] < mais_baixo:
        codigo_mais_baixo = cliente['Código']
        mais_baixo = cliente['Altura']
    if cliente['Peso'] > mais_gordo:
        codigo_mais_gordo = cliente['Código']
        mais_gordo = cliente['Peso']
    if cliente['Peso'] < mais_magro:
        codigo_mais_magro = cliente['Código']
        mais_magro = cliente['Peso']

for cliente in clientes:
    total_altura += cliente['Altura']
    total_peso += cliente['Peso']

print("O cliente {} é o mais alto, possuindo a altura de {}m de altura"
      .format(codigo_mais_alto, mais_alto))
print("O cliente {} é o mais baixo, possuindo a altura de {}m de altura"
      .format(codigo_mais_baixo, mais_baixo))
print("O cliente {} é o mais pesado, possuindo o peso de {}kg"
      .format(codigo_mais_gordo, mais_gordo))
print("O cliente {} é o menos pesado, possuindo o peso de {}kg"
      .format(codigo_mais_magro, mais_magro))
print("A altura média dos clientes é de {}m de altura."
      .format(total_altura / len(clientes)))
print("O peso médio dos clientes é de {}kg."
      .format(total_peso / len(clientes)))
