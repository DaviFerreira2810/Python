# Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
boletim = dict()
boletim['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
elif 5 <= boletim['Média'] < 7:
    boletim['Situação'] = 'Recuperação'
else:
    boletim['Situação'] = 'Reprovado'
print('-=' * 20)
for k, v in boletim.items():
    print(f'{k} é igual a {v}')
# print(f'- Nome é igual a {boletim["Nome"]}')
# print(f'- Média é igual a {boletim["Média"]}')
# print(f'- Situação é igual a {boletim["Situacao"]}')
