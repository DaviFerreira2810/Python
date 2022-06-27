#Desafio 013
#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário,
#com 15% de aumento.

nome = str(input('Digite o nome do funcionário que terá o salário alterado: '))
salario = float(input('Digite o Valor do Salário do {}: R$' .format(nome)))
aumento = salario + (salario * 0.15)

print('O valor do salário do {} com aumento será: R${}' .format(nome, aumento))