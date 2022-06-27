# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
tmaior = 0
tmenor = 0
for c in range(1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
    idade = ano - nasc
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
print('\nNo total {} pessoas são maiores de idade,'.format(tmaior))
print('E {} pessoas são menores de idade!'.format(tmenor))
