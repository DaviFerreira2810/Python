# Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Eu sorteei os valores {n[0]}, {n[1]}, {n[2]}, {n[3]}, {n[4]}.')
ordem = sorted(n)
print(f'O maior número sorteado é o: {ordem[4]}/{max(n)}')
print(f'O menor número sorteado é o: {ordem[0]}/{min(n)}')
