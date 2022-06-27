#Desafio 005
#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor
#e o seu antecessor.

n = int(input('Digite um Número: '))
ant = n - 1
suc = n + 1
print('O número Antecessor de {} é: {} e o Sucessor é: {}'.format(n, ant, suc))

#Outra forma de fazer o programa sem criar mais que uma variavel.

n = int(input('Digite um Número:'))
print('O número antecessor de {} é: {} e o Sucessor é: {}'. format(n, (n-1), (n+1)))