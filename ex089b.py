# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.
print(f'={"-=" * 30}\n{"BOLETIM ESCOLAR": ^60}\n={"-=" * 30}')
lista = list()
while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    opcao = str(input('Deseja continuar [S/N]: '))
    if opcao in 'Nn':
        break
print(lista)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>9}\n{"-" * 25}')
for d, e in enumerate(lista):
    print(f' {d:<4}{e[0]:<10}{e[2]:>8.1f}')
print('-' * 25)
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('-' * 25)
