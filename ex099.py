# Faça um programa que tenha uma função chamada maior(), que receba vários
# parâmetros com valores inteiros. Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior.
from random import randint
from time import sleep
nums = list()
c = 0


def maior(* lista):
    num1 = cont = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in lista:
        print(f'{valor} ', end='')
        sleep(0.25)
        if cont == 0:
            num1 = valor
        else:
            if valor > num1:
                num1 = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado é o {num1}.')


def maiorlista(lista):
    num1 = cont = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in lista:
        print(f'{valor} ', end='')
        sleep(0.25)
        if cont == 0:
            num1 = valor
        else:
            if valor > num1:
                num1 = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado é o {num1}.')


# Programa principal:
while True:
    fim = randint(1, 10)
    if fim >= 0:
        break
while True:
    n = randint(0, 10)
    nums.append(n)
    c += 1
    if c == fim:
        break
maiorlista(nums)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
