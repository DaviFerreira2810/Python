#Escreva um programa que pergunte o salário de um funcionário e
#calcule o valor do seu aumento. Para salários superiores a R$1250,00,
#calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o valor do seu Salário: R$'))
if salario > 1250.00:
    aumento = salario * 0.10
    print('Seu aumento vai ser de R${:.2f}, seu salário será de R${}'.format(aumento, salario + aumento))
else:
    aumento = salario * 0.15
    print('Seu aumento vai ser de R${:.2f}, seu salário será de R${}'.format(aumento, salario + aumento))
