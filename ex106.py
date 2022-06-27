# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai
# digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
# ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep


def pythonHelp(msg):
    print('\033[7;49;97m')
    help(msg)
    print('\033[m', end='')


print(f'\033[7;49;32m{"~" * 25}\n SISTEMA DE AJUDA PYTHON \n{"~" * 25}\n\033[m', end='')
while True:
    opc = str(input('Função ou Biblioteca > ')).lower().strip()
    if opc == 'fim':
        break
    else:
        print(f'\033[7;49;34m{"~" * 36}\n Acessando o Manual do comando {opc} \n{"~" * 36}\n\033[m', end='')
        sleep(2)
        pythonHelp(opc)
print(f'\033[7;49;31m{"~" * 30}\n ATÉ LOGO \n{"~" * 30}\n\033[m')
