n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o segundo número '))
if n1 > n2:
    print(f'O número {n1} é maior que o {n2}')
elif n2 > n1:
    print(f'O número {n2} é maior que o {n1}')
elif n1 == n2:
    print(f'Os dois números são iguais')