# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = par3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matrix[l][c] % 2 == 0:
            # par.append(matrix[l][c]) <- poderia ser essa opção também
            par += matrix[l][c]
        if l == 1:
            if matrix[l][c] > maior:
                maior = matrix[l][c]
        if c == 2:
            # par3.append(matrix[l][c]) <- poderia ser essa opção também
            par3 += matrix[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares digitados é {par}.')
print(f'A soma de todos os valores da linha 3 é {par3}.')
print(f'O maior valor da 2º linha é {maior}.')
