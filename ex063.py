# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência
# de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
cont = 3 #começa no 3 pq ja tem o t1 e o t2.
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print(' → Acabou')