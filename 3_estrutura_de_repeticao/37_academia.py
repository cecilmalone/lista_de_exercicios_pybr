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

clientes = {}

codigo = int(input("Informe o código: "))

if codigo != 0:
    altura = float(input("Informe a altura: "))
    peso = float(input("Informe o peso: "))

    clientes[codigo]['peso'] = peso
    clientes[codigo]['altura'] = altura

    while 0 not in clientes:
        codigo = int(input("Informe o código: "))
        if codigo != 0:
            altura = float(input("Informe a altura: "))
            peso = float(input("Informe o peso: "))

            clientes[codigo]['peso'] = peso
            clientes[codigo]['altura'] = altura

print(clientes)

print (my_dict["my_key"]["key_1"]) // This will print value_1
print (my_dict["my_key"]["key_2"]) // This will print value_2