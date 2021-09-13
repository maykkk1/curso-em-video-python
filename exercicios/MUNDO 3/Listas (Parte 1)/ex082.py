lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    end = ' '
    while end not in 'NS':
        end = str(input('Deseja continuar?[S/N] ')).upper()
    if end == 'N':
        break

for n in lista:
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print(f'A lista principal é: {lista}\n'
      f'Lista com números pares: {lista_par}\n'
      f'Lista com números ímpares: {lista_impar} ')