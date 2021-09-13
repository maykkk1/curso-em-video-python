from time import sleep

números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    x = int(input('Digite um número entre 0 e 20: '))
    if 0 <= x <= 20:
        print(f'Você digitou o número {números[x]}')
        sleep(0.5)
        c = ' '
        while c not in 'SN':
            c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if c == 'N':
            break


