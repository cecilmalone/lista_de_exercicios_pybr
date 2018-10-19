"""
3. Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("Informe o nome: ")
while len(nome) <=3: 
    nome = input("Informe o nome: ")
idade = int(input("Informe a idade: "))
while (idade < 0) or (idade > 150): 
    idade = int(input("Informe a idade: "))
salario = float(input("Informe o salário: "))
while salario <= 0: 
    salario = float(input("Informe o salário: "))
sexo = input("Informe o sexo: ")
while sexo != 'f' and sexo != 'm':
    sexo = input("Informe o sexo: ")
estado_civil = input("Informe o estado civil: ")
while estado_civil not in ('s', 'c', 'v', 'd'): 
    estado_civil = input("Informe o estado civil: ")

print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)
