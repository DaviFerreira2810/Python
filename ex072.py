# Crie um programa que tenha uma dupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte. Seu programa deverá
# ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete')
num2 = ('oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze')
num3 = ('quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numeros = num1 + num2 + num3

while True:
    n = int(input('Digite um número de 0 à 20: '))
    if 0 < n < 20:
        break
    print('Tente Novamente. ', end='')
print(f'Você digitou o número {numeros[n]}')
