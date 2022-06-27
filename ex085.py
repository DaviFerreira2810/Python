# Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
nums = [[], []]
num = 0
for a in range(1, 8):
    num = int(input(f'Digite o {a}° número: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
print(f'Os valores pares são: {sorted(nums[0])}')
print(f'Os valores impares são: {sorted(nums[1])}')
