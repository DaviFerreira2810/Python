# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

print('-=-=' * 12)
print(' Calculadora de IMC - Indice de Massa Corpórea')
print('-=-=' * 12)

peso = float(input('Digite o seu Peso: '))
altura = float(input('Digite a sua Altura (em Metros 0.00): '))
imc = peso / (altura * altura)

print('O seu IMC é de {:.1f}Kg/m²'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está no Peso IDEAL!')
elif 25 <= imc < 30:
    print('Você está SOBREPESO!')
elif 30 < imc <= 40:
    print('Você está na OBESIDADE!')
elif imc > 40:
    print('Você está na OBESIDADE MÓRBIDA!')
