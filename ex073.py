# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

brasil = ('São Paulo', 'Coritiba', 'Corinthians', 'Atlético-MG', 'Ceará',
          'Avaí', 'Cuiabá', 'Juventude', 'Bragantino', 'Flamengo', 'Atlético-GO',
          'Santos', 'Fluminense', 'Palmeiras', 'Fortaleza', 'América-MG', 'Botafogo',
          'Internacional', 'Goiás', 'Athletico-PR')
print('G-5:')
print(brasil[:5])
print('-=' * 35)
print('Z-4:')
print(brasil[-4:])
print('-=' * 47)
print('Ordem Alfabética:')
print(sorted(brasil))
print('-=' * 47)
print(f'Chapecoense está na {brasil.index("Juventude")+1}ª posição!')
