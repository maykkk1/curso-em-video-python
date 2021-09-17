def dobro(n=0, form=False):
    res = 2 * n
    return res if not form else moeda(res)


def metade(n=0, form=False):
    res = n / 2
    return res if not form else moeda(res)


def aumentar(n=0, p=0, form=False):
    res = n + n * (p/100)
    return res if not form else moeda(res)


def diminuir(n=0, p=0, form=False):
    res = n - n * (p/100)
    return res if not form else moeda(res)


def moeda(n, m='R$'):
    fN = f'{m}{n:.2f}'.replace('.', ',')
    return fN


def resumo(num=0, d=0, a=0):
    print('-'*30)
    print('{:^30}'.format('RESUMO DO VALOR'))
    print('-'*30)
    print('{:<20}'.format('Preço analisado: '), '{:<10}'.format(f'{moeda(num)}'))
    print('-' * 30)
    print('{:<20}'.format('Dobro do preço: '), '{:<10}'.format(f'{dobro(num, True)}'))
    print('{:<20}'.format('Metade do preço: '), '{:<10}'.format(f'{metade(num, True)}'))
    print('{:<20}'.format(f'{a}% de Aumento: '), '{:<10}'.format(f'{aumentar(num, a, True)}'))
    print('{:<20}'.format(f'{d}% de Redução: '), '{:<10}'.format(f'{diminuir(num, d, True)}'))
