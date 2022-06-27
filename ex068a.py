# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o
# total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
from time import sleep

print('-=' * 7)
print('\033[1;34m PAR OU IMPAR\033[m')
print('-=' * 7)
resultado = ''
opcao = ''
count = 0
while resultado == opcao:
    opcao = str(input('Par ou Ímpar [P/I]? ')).upper()
    print('1', end=' ')
    print('2', end=' ')
    print('3', end=' ')
    print('e...', end=' ')
    sleep(1.3)
    print('Já')
    user = int(input('Diga um Valor: '))
    pc = randint(0, 10)
    soma = user + pc
    print('-=' * 25)
    if soma % 2 == 0:
        resultado = 'P'
        print(f'Você jogou {user} e eu joguei {pc}. Total deu {soma}, {soma} é PAR')
        print('-=' * 25)
    else:
        resultado = 'I'
        print(f'Você jogou {user} e eu joguei {pc}. Total deu {soma}, {soma} é ÍMPAR')
        print('-=' * 25)
    if resultado == opcao:
        print('\033[1;32m                  VOCÊ VENCEU!!!\033[m')
        print('-=' * 25)
        count += 1
    else:
        print('\033[1;31m                  VOCE PERDEU!!!\033[m')
        print('-=' * 25)
if count == 0:
    print('Você Venceu nenhuma vez!')
elif count == 1:
    print(f'Você Venceu {count} vez!')
elif count > 1:
    print(f'Você Venceu {count} vezes!')