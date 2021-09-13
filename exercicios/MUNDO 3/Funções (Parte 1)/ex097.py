def escreva(msg):
    size = len(msg) + 4
    print('~' * size)
    print(msg.center(size, ' '))
    print('~' * size)


frase = str(input('Digite um texto: '))

escreva(frase)