n = ()
soma = 0
count = 0
while n != 999:
    n = int(input('Digite um número [999 PARA PARAR]: '))
    if n != 999:
        soma += n
        count += 1
if count == 1:
    print(f'Você digitou apenas o número {soma}.')
else:
    print(f'Você digitou {count} números e a soma entre eles é {soma} ')

