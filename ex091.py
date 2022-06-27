#  Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#  Guarde esses resultados em um dicionário em Python. No final,
#  coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

sorteio = dict()
for c in range(1, 5):
    sorteio[f'Jogador{c}'] = randint(1, 6)
print(f'{"-=" * 20}\n{"Jogo do Dado": ^40}\n{"-=" * 20}')
ranking = list()
for k, v in sorteio.items():
    sleep(0.1)
    print(f' O {k} tirou {v} no dado.')
# sleep(2)
print(f'{"-=" * 20}\n{"  == RANKING DOS JOGADORES =="}')
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f"{i + 1}º lugar: {v[0]} tirou {v[1]} no dado.")
