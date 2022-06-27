# Desafio 010
# Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre
# quantos dolares ela pode comprar.
# Considere US$1,00 = R$3,27.

saldo = float(input('Qual o Valor você tem na carteira: R$'))
sldcvt = saldo / 3.27
print('O seu saldo convertido para dolar é USD${:.2f}' .format(sldcvt))
