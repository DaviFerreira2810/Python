# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
soma = prodmil = 0
print('-' * 45)
print('{: ^45}'.format("Davi'Shops"))
print('-' * 45)
produto = str(input('Nome do Produto: ')).strip()
preco = float(input('Preço: R$'))
opcao = ' '
preco2 = precob = preco
barato = produto
while True:
    soma += preco
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]: ')).strip().upper()
    if opcao == 'N':
        break
    if preco >= 1000:
        prodmil += 1
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    if preco < preco2:
        barato = produto
        precob = preco
    opcao = ' '
print('{:-^45}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${soma}')
print(f'Temos {prodmil} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${precob}')
