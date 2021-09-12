lista = [[], [], []]
pos = 0

for elemento in lista:
    for n in range(0,3):
        lista[pos].append(int(input('Digite um número: ')))
    pos += 1

for x in lista:
    for y in x:
        print('[', '{:^3}'.format(f'{y}'),  ']', end=' ')
    print('')