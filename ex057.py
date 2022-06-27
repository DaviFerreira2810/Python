# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite novamente [M/F]? ')).upper()
if sexo == 'M':
    print('Você é do sexo MASCULINO!')
else:
    print('Você é do sexo FEMININO!')

