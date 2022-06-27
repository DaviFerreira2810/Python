# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
num = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    num.append(n)
    if n % 2 == 0 and n != 0:
        par.append(n)
    else:
        impar.append(n)
    opcao = str(input('Deseja Continuar [S/N]: ')).lower()
    if opcao == 'n':
        break
print(f'Lista de números digitados: {num}')
print(f'Lista de números pares: {par}')
print(f'Lista de números impares: {impar}')
