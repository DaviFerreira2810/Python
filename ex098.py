# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def lin():
    print('-=' * 25)


lin()


def contador(inicio, fim, passo):
    if passo < 0:
        if passo == -10:
            print(f'Contagem de {inicio} até {fim + 2} de {passo * -1} em {passo * -1}:')
        else:
            print(f'Contagem de {inicio} até {fim} de {passo * -1} em {passo * -1}:')
    else:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if fim > 0:
        fim += 1
    else:
        fim -= 1
    if passo == 0:
        passo += 1
    if inicio > fim and passo == -1:
        fim -= 2
    if inicio > fim and passo == -1 and fim < 0:
        fim += 2
    for c in range(inicio, fim, passo):
        sleep(0.25)
        print(c, end=' ')
    print('FIM!')


contador(1, 10, 1)
lin()
contador(10, 0, -2)
lin()
print('Agora é sua vez de personalizar a contagem!')
print('Digite um número para...')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if i < f and p < 0:
    p *= -1
if f < i and p == 10:
    f -= 2
if p == 0:
    p = 1
if f < i:
    if p > 0:
        p *= -1
if i == 0 and f == 0:
    p = 0
contador(i, f, p)
