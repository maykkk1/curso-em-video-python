from time import sleep


def maior(*x):
    size = len(x)
    maior = 0
    print('=-' * 30)
    print('Analisando os valores passados...')
    sleep(1.5)
    if size > 0:
        for i in x:
            if i > maior:
                maior = i
            print(i, end=' ')
        print(f'foram informados. {size} valores ao todo.')
        print(f'O maior valor informado foi {maior}')
    else:
        print('Não foi informado valor algum.')


maior(1, 3, 4)
maior(5, 6, 9, 8, 5)
maior(0, 1, 3, 5)
maior(5, 2, 6, 10)
maior()



