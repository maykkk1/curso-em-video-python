count = 0
soma = 0
biggest = 0
c = ()
while c != 'N':
    c = ()
    n = int(input('Digite um número: '))
    if count == 0:
        smallest = n
    if n > biggest:
        biggest = n
    if n < smallest:
        smallest = n
    soma += n
    count += 1
    while c != 'N' and c != 'S':
        c = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if c != 'N' and c != 'S':
            print('Opção inválida, digite novamente!')
print('Você digitou {} números e a média foi {:.2f}.'.format(count, soma/count))
print(f'O maior valor foi {biggest} e o menor foi {smallest}.')
