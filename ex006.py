#Desafio 006
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um Número: '))
db = n * 2
tri = n * 3
raiz = n ** (1/2)

print('O dobro de {} é: {} \nO triplo de {} é: {} \nA raiz quadrada de {} é: {:.3f}'.format(n, db, n, tri, n, raiz))

#Outra forma de fazer o programa sem criar mais que uma variavel.

n = int(input('Digite um Número: '))

print('O dobro de {} é: {}'.format(n, (n*2)))
print('O triplo de {} é: {} \nA raiz quadrada de {} é: {:.3f}'.format(n, (n*3), n, (n**(1/2))))
