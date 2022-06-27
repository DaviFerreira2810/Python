# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuário se ele quer ou não continuar a digitar valores.

c = ''
nums = maior = menor = soma = 0
while c != 'N':
    n = int(input('Digite um Número: '))
    soma += n
    nums += 1
    if nums == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = str(input('Quer continuar [S/N]? ')).upper()
media = (soma / nums)
print('Foram digitados {} números e a média entre eles foi {}'.format(nums, media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))
