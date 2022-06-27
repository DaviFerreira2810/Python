#Exercicio 014: Escreva um programa que converta uma temperatura digitando
#em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a Temperatura em Celsius: '))
f = (c * (9/5) + 32)

print('A temperatura de {}ºC corresponde à {} ºF (Fahrenheit)'.format(c, f))