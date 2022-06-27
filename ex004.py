#Faça um Programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possiveis sobre ela

#n = input('Digite algo: ')
#print(('O tipo primitivo desse valor é: '), type(n))
#print(('Só tem espaços? '), n.isspace())
#print(('É um número? '), n.isnumeric())
#print(('É alfabético? '), n.isalpha())
#print(('É alfanumérico? '), n.isalnum())
#print(('Está em maiúsculas? '), n.isupper())
#print(('Está em minúsculas? '), n.islower())
#print(('Está em Capitalizada? '), n.istitle())

n = input('Digite algo: ')
print(('O tipo primitivo desse valor é: '), type(n))
print((f'Só tem espaços? {n.isspace()}. É um número? {n.isnumeric()}. É alfabético? {n.isalpha()}.'))
print((f'É alfanumérico? {n.isalnum()}. Está em maiúsculas? {n.isupper()}. Está em minúsculas? {n.islower()}.'))
print(('Está em Capitalizada? '), n.istitle())
