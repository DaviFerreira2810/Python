from time import sleep


def lin():
    print('-=' * 25)


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    lin()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(0.01)

    if inicio < fim:
        cont = inicio
        tab = 0
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.25)
            cont += passo
            tab += 1
            if tab == 15:
                print()
                tab = 0
        print('FIM!')
    else:
        cont = inicio
        tab = 0
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.25)
            cont -= passo
            tab += 1
            if tab == 15:
                print()
                tab = 0
        print('Fim!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
print('Digite um número para...')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
