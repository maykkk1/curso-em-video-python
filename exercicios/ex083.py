expressão = str(input('Digite a expressão: ')).replace(' ', '').replace('', ' ').split()
check = False
par = list()

while True:
    for i in expressão:
        if i == '(' or i == ')':
            par.append(i)
    if len(par) % 2 != 0:
        break
    for pos, x in enumerate(par):
        if pos % 2 == 0:
            if x != '(':
                break
        else:
            if x != ')':
                break
    check = True
    break


if not check:
    print('Essa expressão é inválida!')
else:
    print('Essa expressão é válida.')




