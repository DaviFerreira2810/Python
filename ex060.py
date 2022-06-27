# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input('Digite um número para calcular o seu Fatorial: '))
n = num
f = 1
print('Calculando {}! = '.format(n), end='')
while n > 0:
    print('{}'.format(n), end=' ')
    if n > 1:
        print('x ', end='')
    else:
        print('= ', end='')
    f *= n
    n -= 1
print('{:.2f}'.format(f))
