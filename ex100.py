# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.
from time import sleep
from random import randint

numeros = list()


def sorteia():
    c = 0
    while c <= 5:
        num = randint(0, 20)
        sleep(0.7)
        print(f'{c+1}º Número: {num}')
        numeros.append(num)
        c += 1


def somaPar():
    soma = 0
    for s in numeros:
        if s % 2 == 0:
            soma += s
    print(f'Somando os valores pares da lista temos: {soma}.')


print('Sorteando Valores...')
sleep(2)
sorteia()
print(f'\nA lista dos números sorteados são: {numeros}')
somaPar()
