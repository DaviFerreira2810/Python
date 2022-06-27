# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

i = sm = idadef = 0
print('=' * 25)
print('   CADASTRO DE PESSOAS')
print('=' * 25)
while True:
    sexo = opcao = ' '
    idade = int(input('Idade: '))
    while sexo not in 'M/F':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
        print('=' * 25)
    while opcao not in 'S/N':
        opcao = str(input('Quer Continuar [S/N]? ')).strip().upper()
        print('=' * 25)
    if idade > 18:
        i += 1
    if sexo == 'M':
        sm += 1
    if sexo == 'F' and idade < 20:
        idadef += 1
    if opcao == 'N':
        break
print(f'{i} pessoas são maiores de 18 anos!')
print(f'{sm} Homens cadastrados!')
print(f'{idadef} Mulheres cadastradas menores de 20 anos!')
