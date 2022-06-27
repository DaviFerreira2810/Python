#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome Completo: ')).strip()
caps = nome.upper()
baixo = nome.lower()
nome2 = nome.split()
nomex = ''.join(nome2)
letras = len(nomex)
print('Seu nome em Letra Maiúscula é: {}'.format(caps))
print('Seu nome em Letra Minúscula é: {}'.format(baixo))
print('Seu nome tem: {} letras'.format(letras))
#print('Seu nome tem: {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome é {} e tem {} letras'.format(nome2[0], nome.find(' ')))