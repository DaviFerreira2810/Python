# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’)
# Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def titulo(msg):
    tam = len(msg) + 2
    print(f'{"=" * tam}\n{msg: ^{tam}}\n{"=" * tam}')


titulo('Davi Ferreira')
titulo('Olá, Mundo!')
titulo('Curso de Python no YouTube')
