# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumentar(p):
    aumento = (p * 0.10) + p
    return aumento


def diminuir(p):
    reducao = p - (p * 0.13)
    return reducao


def dobro(p):
    dobrar = p * 2
    return dobrar


def metade(p):
    dividir2 = p / 2
    return dividir2
