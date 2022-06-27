# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
dados = list()
gols2 = list()
info = dict()
total = espaco = esp = 0
while True:
    info['Jogador'] = str(input('Nome do Jogador: ')).capitalize().strip()
    while True:
        partidas = str(input(f'Quantas partidas {info["Jogador"]} jogou? '))
        if partidas in '1234567890':
            partidas = int(partidas)
            if partidas < 11:
                break
    for c in range(1, partidas + 1):
        while True:
            gols = str(input(f'    Quantos gols na partida {c}: '))
            if gols in '1234567890':
                gols = int(gols)
                break
        total += gols
        gols2.append(gols)
    info['Gols'] = gols2.copy()
    info['Total'] = total
    dados.append(info.copy())
    gols2.clear()
    opcao = str(input('Deseja Continuar [S/N]: '))
    if opcao in 'Nn':
        break
print(f'{"-=" * 30}')
for k, v in enumerate(dados):
    if len(v['Gols']) >= 5:
        espaco = len(v['Gols'])
if espaco > 5:
    esp = espaco + 20
else:
    esp = 15
print(f' {"Cod": <4} {"Nome": <15}{"Gols": <{esp}}{" Total": <15}')
if esp >= 20:
    print(f'{"-" * 60}')
else:
    print(f'{"-" * 45}')
for k, v in enumerate(dados):
    if v['Total'] == 0:
        print(f'  {k: <3} {v["Jogador"]: <15}{"Não Fez Gol": <{esp}} {v["Total"]: <15}')
    else:
        print(f'  {k: <3} {v["Jogador"]: <15}{str(v["Gols"]): <{esp}} {v["Total"]: <15}')
print(f'{"-=" * 30}')
while True:
    opc = str(input('Mostrar dados de qual Jogador? (999 interrompe): '))
    if opc == '999':
        print('FINALIZANDO...')
        break
    if opc in '1234567890':
        opc = int(opc)
        if opc >= len(dados):
            print(f'ERRO! Não existe jogador com o código {opc}')
        else:
            print(f' -- LEVANTAMENTO DO JOGADOR {dados[opc]["Jogador"]} -- ')
            for k, v in enumerate(dados):
                if v['Total'] == 0:
                    print(f'{dados[opc]["Jogador"]} não fez gol na Temporada!')
                else:
                    for i, g in enumerate(dados[opc]["Gols"]):
                        print(f'No Jogo {i+1} fez {g} gols.')
print(f'{"-=" * 30}')
