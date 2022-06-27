#Escreva um programa em Python que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.

print('-=-=' * 7)
print('CONVERSOR DE BASES NUMÉRICAS')
print('-=-=' * 7)

num = int(input('Digite um número inteiro: '))
print('''Digite: 1 - CONVERTER PARA BINÁRIO
        2 - CONVERTER PARA OCTAL
        3 - CONVERTER PARA HEXADECIMAL''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é: {}'.format(num, hex(num)[2:]))
else:
    print('Está opção não existe!')
