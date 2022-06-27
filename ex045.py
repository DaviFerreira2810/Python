# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint
print('Suas opções: ')
print("""
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA """)
user = int(input('Qual será sua jogada? '))
pc = randint(0, 2)
if user == 0 or user == 1 or user == 2:
    print('JO')
    sleep(1.5)
    print('KEN')
    sleep(1)
    print('PO!!!')
    if user == pc:
        print('EMPATE!')
    if user == 0 and pc == 1:
        print('Computador jogou PAPEL e você PEDRA')
        print('VOCÊ PERDEU!!')
    if user == 0 and pc == 2:
        print('Computador jogou TESOURA e você PEDRA')
        print('PARÁBENS VOCÊ GANHOU!!!')
    if user == 1 and pc == 0:
        print('Computador jogou PEDRA e você PAPEL')
        print('PARÁBENS VOCÊ GANHOU!!!')
    if user == 1 and pc == 2:
        print('Computador jogou TESOURA e você PAPEL')
        print('VOCÊ PERDEU!!')
    if user == 2 and pc == 0:
        print('Computador jogou PEDRA e você TESOURA')
        print('VOCÊ PERDEU!!')
    if user == 2 and pc == 1:
        print('Computador jogou PAPEL e você TESOURA')
        print('PARÁBENS VOCÊ GANHOU!!!')
else:
    print('Jogada Inválida!!!')

