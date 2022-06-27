#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor do Imóvel: R$'))
salario = float(input('Qual o valor do seu salário: R$'))
tempo = float(input('Quantos anos de financiamento: '))

parcela = casa / (tempo * 12)
saldo = salario * 0.30

print('{:.2f} /// {:.2f}'.format(parcela, saldo))
if saldo >= parcela:
    print('EMPRÉSTIMO APROVADO')
else:
    print('EMPRÉSTIMO NEGADO.')
