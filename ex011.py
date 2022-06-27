#Desafio 011
#Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua
#area e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
#de tinta, pinta uma area de 2m².

alt = float(input('Digite a Altura: '))
larg = float(input('Digite a Largura: '))
area = alt * larg
ltinta = area / 2
print('Você precisaria de {} litros de Tinta.'.format(ltinta))
