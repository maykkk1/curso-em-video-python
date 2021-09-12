n = count = s = 0

while True:
    n = int(input('Digite um némero[DIGITE 999 PARA PARAR]: '))
    if n == 999:
        break
    s += n
    count += 1
print(f'Você digitou {count} números e a soma dos valores é {s}')