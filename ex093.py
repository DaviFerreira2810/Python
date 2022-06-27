# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total
# de gols feitos durante o campeonato.
info = dict()
gols2 = list()
total = 0
info['Jogador'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {info["Jogador"]} jogou? '))
info['Partidas'] = partidas
for c in range(1, partidas + 1):
    gols = int(input(f'    Quantos gols na partida {c}: '))
    total += gols
    gols2.append(gols)
info['Gols'] = gols2
info['Total'] = total
print(f'{"-=" * 30}')
for k, v in info.items():
    print(f'O campo {k} tem o valor {v}')
print(f'{"-=" * 30}')
print(f'O jogador {info["Jogador"]} jogou {partidas} partidas.')
for i, v in enumerate(gols2):
    print(f'    Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {info["Total"]} gols.')
