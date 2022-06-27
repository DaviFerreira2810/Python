# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.
print(f'={"-=" * 30}\n{"BOLETIM ESCOLAR": ^60}\n={"-=" * 30}')
lista = list()
nomes = list()
notas = list()
opcao = nome = ' '
media = c = 0
while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    nomes.append(nome)
    notas.append(media)
    lista.append(nomes[:])
    lista.append(notas[:])
    notas.clear()
    nomes.clear()
    opcao = str(input('Deseja continuar [S/N]: '))
    if opcao in 'Nn':
        break
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>9}\n{"-" * 25}')
for d, e in enumerate(lista):
    if d % 2 == 0:
        print(f' {c:<4}{e[0]:<10}{lista[1][0]:>8.1f}')
        c += 1
print("-" * 25)