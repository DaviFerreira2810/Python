#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
ano = int(input('Digite o Ano de Nascimento: '))
idade = atual - ano
faltam = 18 - idade
passou = idade - 18

print('Quem Nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade < 18 and faltam != 1:
    print('Ainda faltam {} anos para o seu Alistamento!'.format(faltam))
    print('Seu Alistamento será em {}'.format(atual + faltam))
elif idade < 18 and faltam == 1:
    print('Falta só 1 ano para o seu Alistamento')
    print('Seu Alistamento será Ano que vem, em {}'.format(atual + faltam))
elif idade == 18:
    print('ATENÇÃO!!! Seu Alistamento é agora em {}'.format(atual + faltam))
elif idade > 18:
    print('ATENÇÃO!!! Sua data de Alistamento foi em {}'.format(atual - passou))
    print('Necessário comparecer na Junta militar urgentemente, para efetuar o alistamento')
