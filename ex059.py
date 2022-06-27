# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
n1 = float(input('Digite o Primeiro valor: '))
n2 = float(input('Digite o Segundo valor: '))
opcao = 0
while opcao != 5:
    print('-=' * 14)
    print('''Escolha uma opção:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Opção: '))
    if opcao == 1:
        print('------\n Soma\n------')
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('-------------\n Multiplicação\n-------------')
        print('{} * {} = {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        print('---------\n O maior\n---------')
        if n1 > n2:
            print('o número {} é maior que o {}'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que o {}'.format(n2, n1))
        else:
            print('Os números são iguais')
    elif opcao == 4:
        print('Informe os números novamente!')
        n1 = float(input('Digite o Primeiro valor: '))
        n2 = float(input('Digite o Segundo valor: '))
    elif opcao == 5:
        print('Fim')
    else:
        print('Opção Inválida, tente novamente!')

