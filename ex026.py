#Faça um programa que leia uma frase pelo teclado
#e mostre quantas vezes aparece a letra “A”, em que posição ela aparece
#a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma Frase: ')).lower().strip()
print('A letra A aparece {} na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
#O '+1' é para o python não considerar o indice 0.
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))