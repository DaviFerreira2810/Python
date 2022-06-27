# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
dados = list()
np = list()
pesada = list()
leve = list()
opcao = ' '
cont = 0
print('{}\n{: ^60}\n{}'.format('-=' * 30, 'Cadastro de Pessoas', '-=' * 30))
while True:
    cont += 1
    np.append(str(input('Nome: ')))
    np.append(float(input('Peso: ')))
    opcao = str(input('Deseja continuar [S/N]: ')).lower()
    dados.append(np[:])
    np.clear()
    if opcao in 'nnãonao':
        break
print(f'\nForam cadastradas {cont} pessoas!')
for p in dados:
    if p[1] >= 100:
        pesada.append(p[0])
    else:
        leve.append(p[0])
print(f'{pesada} são as pessoas mais Pesadas, com +100Kg!')
print(f'{leve} são as pessoas mais leves, com -100Kg')
