def area(x, y):
    a = x * y
    print(f'A área de um terreno {x}x{y} é de {a}m²')


print('-'*50)
print('{:^50}'.format('CONTROLE DE TERRENOS'))
print('-'*50)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)

