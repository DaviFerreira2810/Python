# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from Python.ex107 import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Reduzindo 13% de R${preco}, temos {moeda.diminuir(preco)}')
print(f'Aumentando 10% de R${preco}, temos {moeda.aumentar(preco)}')
