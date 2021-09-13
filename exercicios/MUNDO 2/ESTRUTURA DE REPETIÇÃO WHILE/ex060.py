n = int(input('Digite um número para calcular-mos seu fatorial: '))
c = n
f = n
check = False
while not check:
    c -= 1
    n = c * n
    if c == 1:
        check = True
print(f'{f}! =', end=' ')
for x in range(f, 1, -1):
    print(x, end=' x ')
print(f'1 = {n}')
