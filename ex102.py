# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o
# número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será
# mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=0):
    """
    -> Calcula o Fatorial de um múmero.
    :param num: O número a ser Fatorado.
    :param show: (opcional) Mostrar ou não a conta.
    """
    f = 1
    if show == 1:
        f = 1
        for c in range(num, 0, -1):
            f *= c
            print(f'{c}', end=' ')
            if c > 1:
                print(f'x', end=' ')
            else:
                print('= ', end='')
        print(f'{f}')
    else:
        for c in range(num, 0, -1):
            f *= c
        print(f'Fatorial de {num} é igual a: {f}')


print(f'{"-" * 12} CALCULADORA DE FATORIAL {"-" * 12}')

n = int(input('Digite um Número: '))
resp = int(input('Deseja mostrar a Fatoração? [1-Sim / 2-Não]: '))
fatorial(n, resp)
