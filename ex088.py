# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print(f'={"-=" * 20}\n{"MEGA-SENA": ^41}\n={"-=" * 20}')
jogo = []
num = []
a = c = 0
njogo = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'={"-=" * 20}')
print('Sorteando...')
sleep(1)
while a != njogo:
    for b in range(0, 6):
        n = randint(1, 60)
        num.append(n)
    jogo.append(num[:])
    num.clear()
    a += 1
    sleep(0.5)
    for d, e in enumerate(jogo):
        c += 1
        print(f'Jogo {c}: {e}')
    jogo.clear()
