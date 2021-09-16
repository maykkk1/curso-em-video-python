def leiaInt(msg):
    num = str(input(msg))
    if num.isnumeric():
        return int(num)
    else:
        while True:
            print('\033[:31mErro! Digite um número inteiro válido.\033[m')
            num = str(input('Digite um número: '))
            if num.isnumeric():
                return int(num)


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
