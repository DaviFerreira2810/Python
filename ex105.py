# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional).


def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior Nota'] = max(n)
    r['Menor Nota'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7.0:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'REPROVADO'
    return r


resp = notas(5.5, 8, 6.5, 7, sit=True)
print(resp)
