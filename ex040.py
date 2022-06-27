#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

aluno = str(input('Digite o nome do aluno: ')).title().strip()
nota1 = float(input('Digite a nota da 1ª Prova do {}: '.format(aluno)))
nota2 = float(input('Digite a nota da 2ª Prova do {} '.format(aluno)))

media = (nota1 + nota2) / 2
print('A média do aluno é {:.1f}'.format(media))
if media > 7.0:
    print('{} está APROVADO'.format(aluno))
elif media > 5.0 < 6.9:
    print('{} está de RECUPERAÇÃO'.format(aluno))
else:
    print('{} está REPROVADO'.format(aluno))
