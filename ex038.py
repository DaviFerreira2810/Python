#Escreva um programa que leia dois números inteiros e compare-os.
#mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

print('-=-=' * 5)
print('!Comparando números!')
print('-=-=' * 5)

n1 = float(input('Digite o Primeiro Número: '))
n2 = float(input('Digite o Segundo Número: '))

if n1 > n2:
    print('O primeiro valor é Maior que o segundo!')
elif n2 > n1:
    print('O segundo valor é Maior que o primeiro!')
else:
    print('Os dois valores são IGUAIS!')
