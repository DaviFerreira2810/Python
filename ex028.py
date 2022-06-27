#Escreva um programa que faça o computador “pensar” em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
#número escolhido pelo computador. O programa deverá escrever na tela
#se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
num1 = randint(0, 5)
print('Deixa eu ver...')
sleep(2)
print('Já sei.')
num2 = int(input('Vai lá, diga qual número eu pensei? '))
print('ATENÇÃO...')
sleep(2)
if num2 == num1:
    print('Parabéns você ACERTOU!!!')
else:
    print('HAHAHA, Que pena, você não adivinhou!!!')
