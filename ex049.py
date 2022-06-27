# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
for x in range(100000):
    print('--------------------')
    n = int(input('Digite um numero: '))
    print('---------------')
    print('Tabuada do {}'.format(n))
    for c in range(1, 11):
        print('{} x  {} = {}'.format(n, c, n*c))
