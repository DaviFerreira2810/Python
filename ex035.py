#Desenvolva um programa que leia o comprimento de três retas
#e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 9)
print(' Analisador de Triângulos!')
print('-=-' * 9)
print("""
         / \ 
        /   \ 
     a /     \ b 
      /       \ 
     /_ _ _ _ _\ 
          a """)

la = float(input('Medida do lado a: '))
lb = float(input('Medida do lado b: '))
lc = float(input('Medida do lado c: '))

if (la + lb) > lc and (lb + lc) > la and (lc + la) > lb:
    print('As medidas acima FORMAM um triângulo!!!')
else:
    print('As medidas acima NÃO formam um triângulo!!!')
