import time
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
check = False
while not check:
    print('=-='*13)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    c = int(input('>>>>>Qual é a sua opção? '))
    time.sleep(0.5)
    if c == 1:
        print(f'\033[:1:91mA soma dos números informados é {n1 + n2}\033[m')
    elif c == 2:
        print(f'\033[:1:91mO produto dos números informados é {n1 * n2}\033[m')
    elif c == 3:
        if n1 > n2:
            print(f'\033[:1:91mEntre os números informados o maior é {n1}\033[m')
        else:
            print(f'\033[:1:91mEntre os números informados o maior é {n2}\033[m')
    elif c == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif c == 5:
        check = True
    else:
        print('\033[:1:91mOpção incorreta!\033[m')
print('DESLIGAR')