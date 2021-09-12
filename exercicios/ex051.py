print('=' * 30)
print('     10 Termos de uma PA')
print('=' * 30)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
if n == 0:
    for x in range(n, 10 * r, r):
        print(f'{x} ➔', end=' ')
else:
    for x in range(n, n + (10 * r), r):
        print(f'{x} ➔', end=' ')
print('ACABOU!')
