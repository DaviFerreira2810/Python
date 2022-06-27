#Desafio 008
#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros
#e em milímetros.

print('CONVERSOR DE METROS PARA CENTIMETROS E MILIMETROS')
n = int(input('Digite um valor em metros: '))
cm = n * 100
mm = n * 1000

print('Centimetros: {:.0f}cm'.format(cm))
print('Milimetrso: {:.0f}mm'.format(mm))
