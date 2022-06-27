import random
al1 = str(input('Primeiro Aluno: '))
al2 = str(input('Segundo Aluno: '))
al3 = str(input('Terceiro Aluno: '))
al4 = str(input('Quarto Aluno: '))
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print('O aluno escolhido é: {}'.format(escolhido))