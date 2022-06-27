# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


def ficha(j, g=0):
    if not j:
        j = '<desconhecido>'

    print(f'O jogador {j} fez {g} gol(s) no campeonato.')


# Programa Principal:
jogador = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(jogador, gols)