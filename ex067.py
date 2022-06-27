# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
n = 1
m = n
while True:
    c = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-=' * 23)
    if n < 0:
        break
    while c != 11:
        m = n * c
        print(f'{n} x {c} = {m}')
        c += 1
    print('-=' * 23)
    print('Para sair digite um número negativo.')
print(' PROGRAMA DE TABUADA ENCERRADO. Volte Sempre!')

