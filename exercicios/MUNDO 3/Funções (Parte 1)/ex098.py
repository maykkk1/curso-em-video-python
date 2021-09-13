from time import sleep


def linhas():
    print('-=' * 15)


def título(start, end, step):
    print(f'Contagem de {start} até {end} de {step} em {step}.')


def contador(start, end, step):
    if step < 0:
        step *= (-1)
    print(step)
    if start < end:
        for x in range(start, end + 1, step):
            sleep(0.7)
            print(x, end=' ')
        print('Fim!')
    else:
        for x in range(start, end - 1, step * -1):
            sleep(0.7)
            print(x, end=' ')
        print('Fim!')


linhas()
título(0, 10, 1)
contador(1, 10, 1)
linhas()
título(0, 10, 2)
contador(0, 10, 2)

print('Agora é sua vez de personalizar a contagem.')
while True:
    start = int(input('Começo: '))
    end = int(input('Fim: '))
    step = int(input('Passo: '))
    linhas()
    título(start, end, step)
    contador(start, end, step)
    end = ' '
    while end not in 'SN':
        end = str(input('Deseja continuar? [S/N]')).upper()[0]
        if end in 'SN':
            break
        else:
            print('Erro! Digite S pra continar e N para sair.')
    if end == 'N':
        break
print('Fim do programa.')


