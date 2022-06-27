#screva um programa que pergunte a quantidade de Km percorridos por um
#carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
d = int(input('Quantos Dias alugado? '))
km = int(input('Quantos Km Rodados? '))
aluguel = (60 * d) + (km * 0.15)
print('O valor a ser pago pelo aluguel do veiculo é de: R${:.2f}'.format(aluguel))
