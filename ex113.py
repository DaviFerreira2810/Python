# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[5;49;31mERRO! Digite um número Válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[5;49;31mEntrada de dados Interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[5;49;31mERRO! Digite um número Válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[5;49;31mEntrada de dados Interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


num = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número Real:')
print(f'O valor inteiro digitado foi {num} e o real foi {num2}')
