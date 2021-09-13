produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
title = 'LISTAGEM DE PREÇOS'
print('-'*50)
print(title.center(50))
print('-'*50)
pos_x = 0
pos_y = 1
count = 0
while True:
    print('{:<38}'.format(produtos[pos_x]).replace(' ', '.'),'R$', '{:>8}'.format(f'{produtos[pos_y]:.2f}'))
    count+= 2
    pos_x += 2
    pos_y += 2
    if count == 18:
        break
