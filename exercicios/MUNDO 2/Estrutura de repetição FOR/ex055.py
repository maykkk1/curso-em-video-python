men_p = 0
mai_p = 0
pos_p = 1
check = True
for x in range(0, 5):
    p = float(input(f'Digite o peso da {pos_p}º pessoa: '))
    while check == True:
        men_p = p
        check = False
    if p > mai_p:
        mai_p = p
    if p < men_p:
        men_p = p
    pos_p += 1

if men_p == mai_p:
    print('Todos tem o mesmo peso.')
else:
    print('O maior peso lido foi {:.2f}kg\nO menor peso lido foi {:.2f}kg'.format(mai_p, men_p))
