#Desafio 012
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
#com 5% de desconto.

prdt = float(input('Qual o valor do Produto: R$'))
dscnt = prdt - (prdt * 0.05)
print('O valor do produto com 5% de desconto será: R${}' .format(dscnt))
