# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade.
# C) Uma lista com as mulheres.
# D) Uma lista de pessoas com idade acima da média.
lista = list()
dados = dict()
media = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if dados['sexo'] in 'MF':
            break
    dados['idade'] = int(input('Idade: '))
    media += dados['idade']
    lista.append(dados.copy())
    dados.clear()
    opcao = str(input('Quer Continuar [S/N]: '))
    if opcao in 'Nn':
        break
print(f'{"-=" * 21}')
if len(lista) == 1:
    print(f'Foi cadastrado apenas {len(lista)} pessoa.')
else:
    print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A média de idade é de{media / len(lista): .0f} anos.')
print(f'{"-=" * 5}{" MULHERES CADASTRADAS ": ^10}{"-=" * 5}')
for i, v in enumerate(lista):
    if v['sexo'] == 'F':
        print(f' - {v["nome"]}')
print(f'{"-=" * 5}{" PESSOAS ACIMA DA MÉDIA ": ^10}{"-=" * 5}')
for i, v in enumerate(lista):
    if v['idade'] > (media / len(lista)):
        print(f' - {v["nome"]}')
