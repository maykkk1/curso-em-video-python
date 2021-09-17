def fatorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def double(n):
    res = 2 * n
    return res


def half(n):
    res = n / 2
    return res


def aumentar(n, p):
    res = n + n * (p/100)
    return res


def diminuir(n, p):
    res = n - n * (p/100)
    return res


def moeda(n):
    fN = f'R${n:.2f}'.replace('.', ',')
    return fN