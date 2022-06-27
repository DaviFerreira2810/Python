# Crie um programa que leia nome, ano de nascimento e carteira de
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso
# a CTPS for diferente de ZERO, o dicionário receberá também o ano
# de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.
from datetime import date
ano = date.today().year
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Idade'] = ano - int(input('Ano de Nascimento: '))
dados['CTPS'] = int(input('Nº da Carteira de Trabalho (0 não tem):  '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Contratação'] + 35) - ano + dados['Idade']
print(f'{"-=" * 30}')
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
