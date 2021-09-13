pessoas = list()
pessoa = list()
pesada = list()
leve = list()
count = 0
while True:
    pessoa.append(str(input('Nome: ')).capitalize())
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    count += 1
    pessoa.clear()
    end = ' '
    while end not in 'SN':
        end = str(input('Deseja continuar? ')).upper()
    if end == 'N':
        break

for pos, p in enumerate(pessoas):
    if pos == 0:
        pesada.append(p[:])
        leve.append(p[:])
    if pos != 0:
        if p[1] == pesada[0][1]:
            pesada.append(p[:])
        elif p[1] > pesada[0][1]:
            pesada.clear()
            pesada.append(p[:])
        if p[1] == leve[0][1]:
            leve.append(p[:])
        elif p[1] < leve[0][1]:
            leve.clear()
            leve.append(p[:])

print(f'Você cadastrou {count} pessoas.')
print(f'O maior peso foi {pesada[0][1]}Kg.', end=' ')
print('Peso de', end=' ')
for elemento in pesada:
    if elemento[0] == pesada[-1][0]:
        print(elemento[0], end='.\n')
    elif elemento[0] == pesada[-2][0]:
        print(elemento[0], end=' e ')
    else:
        print(elemento[0], end=', ')

print(f'O menor peso foi {leve[0][1]}Kg.', end=' ')
print('Peso de', end=' ')
for elemento in leve:
    if elemento[0] == leve[-1][0]:
        print(elemento[0], end='.\n')
    elif elemento[0] == leve[-2][0]:
        print(elemento[0], end=' e ')
    else:
        print(elemento[0], end=', ')







