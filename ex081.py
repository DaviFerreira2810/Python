# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre: A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
num = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    cont += 1
    opcao = str(input('Deseja continuar [S/N]: ')).lower()
    if opcao == 'n':
        break
print(f'Foram digitados {cont} números.')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
