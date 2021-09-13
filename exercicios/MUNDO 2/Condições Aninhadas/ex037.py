n = int(input('Digite um numero inteiro '))
print('Escolha uma das bases para conversão ')
print('[ 1 ] para BINÁRIO')
print('[ 2 ] para OCTAL')
print('[ 3 ] para HEXADECIMAL')
c = int(input('Sua opção '))
if c == 1:
    n = format(n, 'b')
    print(n)
elif c == 2:
    n = format(n, 'o')
    print(n)
elif c == 3:
    n = format(n, 'X')
    print(n)
else:
    print("Opção inválida! Tente novamente.")



