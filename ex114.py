# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Erro ao carregar o site.')
else:
    print('O site carregou corretamente.')
