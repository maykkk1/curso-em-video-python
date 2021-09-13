tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite um número: ')))
f9 = str(tupla).find('9')
f3 = str(tupla).find('3')

if f9 >= 0:
    print(f'O valor 9 apareceu {tupla.count(9)} vez(es).')
else:
    print(f'O valor 9 não aparece na tupla.')
if f3 >= 0:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não aparece na tupla.')
print('Os números pares foram: ', end='')
for x in tupla:
    if x % 2 == 0:
        print(x, end=' ')
