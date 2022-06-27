#Desafio 007
#Desenvolva um programa que leia as duas notas de um aluno, e mostre a sua média.

nome = input('Digite o nome do Aluno: ')
n1 = float(input('Qual a nota da Prova 1 do {}:'.format(nome)))
n2 = float(input('Qual a nota da Prova 2 do {}:'.format(nome)))
media = (n1+n2)/2

print('A média de {} entre {} e {} é {:.1f}'.format(nome, n1, n2, media))
