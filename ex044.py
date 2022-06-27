# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('========== ANDAJES MARKET ==========')

preco = float(input('Digite o valor da Compra: '))
print('Escolha as formas de Pagamento:')
print('[ 1 ] à vista dinheiro/cheque: 10% de desconto')
print('[ 2 ] à vista no cartão: 5% de desconto')
print('[ 3 ] em até 2x no cartão: preço formal')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')

opcao = int(input('Digite a opção Desejada: '))
dinheiro = preco - (preco * 0.10)
cartao1 = preco - (preco * 0.05)

if opcao == 1:
    print('O valor à vista no dinheiro/cheque é: R${}'.format(dinheiro))
elif opcao == 2:
    print('O valor à vista no cartão é: R${}'.format(cartao1))
elif opcao == 3:
    print('O valor em até 2x no cartão permanece R${}'.format(preco))
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    if parcela == 1:
        print('O valor à vista no cartão é: R${}'.format(preco))
    elif parcela == 2:
        print('O valor em até 2x no cartão permanece R${}'.format(preco))
    elif parcela >= 3:
        valor = preco + (preco * 0.20)
        valor1 = valor / parcela
        print('O valor dividido em {}x fica {} parcelas de R${:.2f}\nNo total vai custar: R${:.2f}'.format(parcela, parcela, valor1, (valor1 * parcela)))
else:
    print('Opção Inválida!')
