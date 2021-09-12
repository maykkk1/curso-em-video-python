lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        loop_escolha = ' '
        while loop_escolha not in 'SN':
            loop_escolha = str(input('Deseja continuar?[S/N] ')).upper()
        if loop_escolha == 'N':
            break
    else:
        print('Esse número já está na lista.')
        loop_escolha = ' '
        while loop_escolha not in 'SN':
            loop_escolha = str(input('Deseja continuar? ')).upper()
        if loop_escolha == 'N':
            break
lista.sort()
print(f'Você digitou os valores {lista}')
