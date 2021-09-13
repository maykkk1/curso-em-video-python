print('Gerador de P.A')
s = 9
t1 = int(input('Digite o primeiro termo: '))
t2 = int(input('Razão da PA: '))
pa = t1
print(pa, end=' ➔ ')
while s > 0:
    pa += t2
    if s == 1:
        print(pa, end=' ➔ FIM!')
    else:
        print(pa, end=' ➔ ')
    s -= 1

