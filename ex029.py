#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do Carro? '))
if velocidade > 80:
    print('Você Ultrapassou o limite de 80Km/h! Está multado!')
    multa = velocidade - 80
    print('O valor da multa é de R${:.2f}'.format(multa * 7))
else:
    print('Parabéns, esta dentro do limite permitido!!!')
