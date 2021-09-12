n = int(input('Digite um número: '))
count = 0
for x in range(1, n + 1):
    if n % x == 0:
        count += 1
        print('\033[::92m', end='')
        print( x, end=' ')
        print('\033[m', end='')
    else:
        print('\033[::91m', end='')
        print( x, end=' ')
        print('\033[m', end='')
print('')
if count == 2:
    print('O número só foi divisível por 1 e por ele mesmo, então é um número PRIMO.')
else:
    print(f'O número foi divisível {count} vezes, então não é um número PRIMO. ')
