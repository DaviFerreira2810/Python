# A Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
from datetime import date

ano = int(input('Digite o ano de nascimento do Atleta: '))

atual = date.today().year
idade = atual - ano

if idade > 0 and idade <= 9:
    print('O atleta com {} anos pertence a Categoria: MIRIM!'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta com {} anos pertence a Categoria: INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta com {} anos pertence a Categoria: JÚNIOR'.format(idade))
elif idade > 19 and idade <= 25:
    print('O atleta com {} anos pertence a Categoria: SÊNIOR'.format(idade))
elif idade > 25:
    print('O atleta com {} anos pertence a Categoria: MASTER'.format(idade))
elif idade <= 0:
    print('Você digitou o ano de nascimento errado!!!')

