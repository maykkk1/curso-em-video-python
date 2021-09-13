lista = []

for x in range(0,5):
    num = int(input('Digite um número: '))
    if x == 0:
        lista.append(num)
        print('Foi adicionado na posição 0')
    if x == 1:
        if num > lista[0]:
            lista.append(num)
            print('O número foi colocado na posição 1')
        else:
            lista.insert(0, num)
            print('O número foi colocado na posição 0')
    if x == 2:
        if num > lista[0] and num > lista[1]:
            lista.append(num)
            print('Foi adicionado na ultima posição')
        elif lista[0] < num < lista[1]:
            lista.insert(1, num)
            print('Foi adiciona na posição 1')
        else:
            lista.insert(0, num)
            print('Foi adicionado na posição 0')
    if x == 3:
        if num > lista[0] and num > lista[1] and num > lista[2]:
            lista.append(num)
            print('Foi adicionado na ultima posição')
        elif num > lista[0] and num > lista[1] and num < lista[2]:
            lista.insert(2, num)
            print('Foi adicionado na posição 2')
        elif lista[0] < num < lista[1]:
            lista.insert(1, num)
            print('Foi adicionado na posição 1')
        else:
            lista.insert(0, num)
            print('Foi adicionado na posição 0')
    if x == 4:
        if num > lista[0] and num > lista[1] and num > lista[2] and num > lista[3]:
            lista.append(num)
            print('Foi adicionando na ultima posição')
        elif num > lista[0] and num > lista[1] and num > lista[2] and num < lista[3]:
            lista.insert(3, num)
            print('Foi adicionado na posição 3')
        elif num > lista [0] and num > lista [1] and num < lista[2]:
            lista.insert(2, num)
            print('Foi adicionado na posição 2')
        elif lista[0] < num < lista[1]:
            lista.insert(1, num)
            print('Foi adicionado na posição 1')
        else:
            lista.insert(0, num)
            print('Foi adicionado na posição 0')













print(lista)