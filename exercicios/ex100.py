from random import randint
from time import sleep


def random_num():
    lista = []
    print('Sorteando 5 valores: ', end=' ')
    for i in range(0, 5):
        i = randint(0, 10)
        print(i, end=' ')
        lista.append(i)
        sleep(0.8)
    print('Pronto!')
    return lista


def somar(x):
    soma = 0
    for i in x:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {x}, temos {soma}')


somar(random_num())