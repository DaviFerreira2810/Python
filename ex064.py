# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).
c = nums = soma = 0
c = int(input('Digite um Número [sair = 999]: '))
while c != 999:
    soma += c
    nums += 1
    c = int(input('Digite um Número [sair = 999]: '))
print('Foram digitados {} números antes de sair'.format(nums))
print('E a soma entre eles é {}'.format(soma))
