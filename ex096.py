# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def titulo(msg):
    print(f'{"=" * (len(msg)+2)}\n{msg: ^{len(msg) + 2}}\n{"=" * (len(msg)+2)}')


titulo('CALCULADORA DE TERRENO')


def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg} x {comp} é de {a}mts')


while True:
    l = str(input(f'Largura (m): '))
    if l in '1234567890':
        l = float(l)
        break
while True:
    c = str(input(f'Comprimento (m): '))
    if c in '1234567890':
        c = float(c)
        break
area(l, c)
