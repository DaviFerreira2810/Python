#Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
print('-=-' * 9)
print('Descubra se o ano é Bissexto')
print('-=-' * 9)
ano = int(input('Digite o Ano desejado, Caso queira avaliar o ano atual digita 0:'))
if ano == 0:
    ano = date.today().year #Vai pegar a tada de hoje(date.today), mas só o ano (.year)
    if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
        print('{} é um ano Bissexto'.format(ano))
    else:
        print('{} não é um ano Bissexto'.format(ano))
else:
    if ano != 0:
        if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
            print('{} é um ano Bissexto'.format(ano))
        else:
            print('Esse ano de {} não é Bissexto'.format(ano))
