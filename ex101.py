# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date
ano = date.today().year

print(f'{"-" * 10} SISTEMA ELEITORAL {"-" * 10}')


def voto(n=0):
    idade = ano - n
    if 65 > idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    elif idade < 16:
        print(f'Com {idade} anos: NÃO VOTA!')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL!')


nasc = int(input('Em que ano você nasceu: '))
voto(nasc)
