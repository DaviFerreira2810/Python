# Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados na ordem correta.
exp = str(input('Digite uma expressão Matemática: '))
pilha1 = []
pilha2 = []
for simb in exp:
    if simb == '(':
        pilha1.append('(')
    elif simb == ')':
        pilha2.append(')')
if len(pilha1) == len(pilha2):
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
