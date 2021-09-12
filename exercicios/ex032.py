from datetime import date
x = int(input('digite o ano '))
if x == 0:
    x = date.today().year
if x > 3:
    r4 = x % 4
    r100 = x % 100
    r400 = x % 400
    if r100 == 0:
        if r400 == 0:
            print('Esse ano é bissexto')
        else:
            print('Esse ano não é bissexto')
    if r4 == 0 and r100 != 0:
        print('Esse ano é bissexto')
    else:
        print('Esse ano não é bissexto')
else:
    print('Esse ano não é bissexto')