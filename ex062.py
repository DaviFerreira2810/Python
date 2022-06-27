# Melhore o DESAFIO 61, perguntando para o usuário
# se ele quer mostrar mais alguns termos. O programa
# encerrará quando ele disser que quer mostrar 0 termos.

print('=' * 21)
print(' 10 TERMOS DE UMA PA ')
print('=' * 21)
n1 = int(input('Primeiro Termo: '))
n2 = int(input('Razão: '))
termo = n1
c = 1
total = 0
termo2 = 10
while termo2 != 0:
    total += termo2
    while c <= total:
        print('{} → '.format(termo), end='')
        termo += n2
        c += 1
    print('PAUSA')
    termo2 = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')

