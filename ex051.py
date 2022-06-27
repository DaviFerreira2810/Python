# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 21)
print(' 10 TERMOS DE UMA PA ')
print('=' * 21)
n1 = int(input('Primeiro Termo: '))
n2 = int(input('Razão: '))
dec = n1 + (10 - 1) * n2
for c in range(n1, dec, n2):
    print(c, end=' → ')
print('ACABOU')