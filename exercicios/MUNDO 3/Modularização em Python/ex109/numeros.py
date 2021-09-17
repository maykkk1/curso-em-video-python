def fatorial(n=0):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def double(n=0, form=False):
    res = 2 * n
    return res if not form else moeda(res)


def half(n=0, form=False):
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