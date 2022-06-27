# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=' * 21)
print(' 10 TERMOS DE UMA PA ')
print('=' * 21)
n1 = int(input('Primeiro Termo: '))
n2 = int(input('Razão: '))
termo = n1
c = 1
while c <= 10:
    print('{} → '.format(termo), end='')
    termo += n2
    c += 1
print('ACABOU')