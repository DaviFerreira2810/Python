# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

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
    if la == lb and lb == lc and lc == la:
        print('Essas medidas PODEM FORMAR um triângulo EQUILÁTERO!')
    elif la == lb and lb != lc and lc != la or la == lc and lc != lb and lb != la or lb == lc and lc != la and la != lb:
        print('Essas medidas PODEM FORMAR um triângulo ISÓSCELES!')
    elif la != lb and lb != lc and lc != la:
        print('Essas medidas PODEM FORMAR um triângulo ESCALENO!')
else:
    print('As medidas acima NÃO formam um triângulo!!!')
