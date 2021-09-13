p1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
check = False
x = 10
p1_check = True
while not check:
    count = x - 1
    while count > 0:
        if p1_check == True:
            print(p1, end=' ➔ ')
            p1_check = False
        p1 += r
        if count == 1:
            print(p1, end=' FIM!')
        else:
            print(p1, end=' ➔ ')
        count -= 1
    print('')
    x = int(input('Quantos termos você quer mostrar a mais? '))
    if x == 0:
        check = True
        print('Fim do programa!')
    else:
        x += 1