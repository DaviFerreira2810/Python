# Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma Frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for l in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[l]
if inverso == junto:
    print('A frase "{}" é um PALÍNDROMO!'.format(inverso))
else:
    print('A frase "{}" não é um PALÍNDROMO!'.format(inverso))

#       print('A frase "{}" é um PALÍNDROMO!'.format(inverso))
#    else:
#       print('A frase "{}" não é um PALÍNDROMO!'.format(inverso))