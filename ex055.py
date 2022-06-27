# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
pmaior = 0
pmenor = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(c)))
    if c == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        else:
            pmenor = peso
print('O maior peso lido foi de {}Kg'.format(pmaior))
print('O menor peso lido for de {}Kg'.format(pmenor))

