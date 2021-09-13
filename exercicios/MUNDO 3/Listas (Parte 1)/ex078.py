lista = []
menor_pos = []
maior_pos = []
for pos, v in enumerate(range(0,5)):
    num = (int(input('Digite um número: ')))
    lista.append(num)
    if pos == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

for pos, x in enumerate(lista):
    if x == menor:
        menor_pos.append(pos)
    if x == maior:
        maior_pos.append(pos)

print(f'O maior número é {maior} e está nas posições: ', end='')
for n in maior_pos:
    print(n, end=' ')
print('')
print(f'O menor número é {menor} e está nas posições: ', end='')
for n in menor_pos:
    print(n, end=' ')
