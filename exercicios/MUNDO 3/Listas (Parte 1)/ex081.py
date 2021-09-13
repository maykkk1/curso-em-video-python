lista = []
v = 'não contém'
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    end = ' '
    while end not in 'SN':
        end = str(input('Deseja continuar?[S/N] ')).upper()
    if end == 'N':
        break
for x in lista:
    if x == 5:
        v = 'contém'
lista.sort(reverse=True)
print(f'A lista tem {len(lista)} números\n'
      f'A lista {v} o número 5\n'
      f'Está é a lista em forma decrescente {lista}')
