# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.
num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com Sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = str(input('Deseja Continuar [S/N]: ')).lower()
    if opcao == 'n':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(num)}')
# se valor digitado for igual a v, digite novamente
