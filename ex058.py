# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
num2 = 0
x = 0
print('-=' * 27)
print(' Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=' * 27)
num1 = randint(1, 11)
print('Deixa eu ver...')
sleep(2)
print('Já sei.')
while num2 != num1:
    num2 = int(input('Vai lá, diga qual número eu pensei? '))
    print('ATENÇÃO...')
    sleep(2)
    if num2 != num1:
        print('HAHAHA, Que pena, você não adivinhou!!!')
        x += 1
    elif num2 == num1:
        print('Parabéns, você tentou {} vezes e ACERTOU!!!'.format(x))
print('FIM')