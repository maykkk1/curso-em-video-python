lista = [[], []]
for x in range(1,8):
    num = int(input(f'Digite o {x}º valor: '))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)

print(f'Lista de números pares: {sorted(lista[0])}\n'
      f'Lista de números ímpares: {sorted(lista[1])}')
