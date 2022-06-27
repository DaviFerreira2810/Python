# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o
# nome do homem mais velho e quantas mulheres têm menos de 20 anos.
idadeM = 0
sexoF = 0
sexoM = 0
Ivelho = 0
Nvelho = ''
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    idadeM += idade
    if sexo == 'F' and idade < 20:
        sexoF += 1
    else:
        if idade > Ivelho:
            Ivelho = idade
            Nvelho = nome
media = idadeM / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(Ivelho, Nvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(sexoF))