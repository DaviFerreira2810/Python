#Faça um programa que leia o comprimento do cateto oposto e do c
#ateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
from math import pow, sqrt

co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto adjacente: '))
#a² + b² = h²
h = sqrt((pow(co, 2)) + (pow(ca, 2)))
print('O valor da hipotenusa é: {:.2f}'.format(h))