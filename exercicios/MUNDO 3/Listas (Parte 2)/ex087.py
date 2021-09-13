lista = [[], [], []]
pos = 0
somaPar = 0
soma3Column = 0
maior2Line = 0

for elemento in lista:
    for n in range(0, 3):
        num = int(input('Digite um número: '))
        if num % 2 == 0:
            somaPar += num
        if n == 2:
            soma3Column += num
        if pos == 1:
            if num > maior2Line:
                maior2Line = num
        lista[pos].append(num)
    pos += 1
for c in lista:
    for l in c:
        print('[', '{:^3}'.format(l), ']', end=' ')
    print('')

print(f'A soma de todos os números pares é {somaPar}\n'
      f'A soma dos números da terceira coluna é {soma3Column}\n'
      f'O maior número da segunda linha é {maior2Line}')