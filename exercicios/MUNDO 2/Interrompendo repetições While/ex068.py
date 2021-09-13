import random
win = True
count = 0
print('Vamos jogar ÍMPAR ou PAR!')
while True:
    n = int(input('Digite um valor de 0 a 10: '))
    c = str(input('P/I: ')).strip().upper()
    if n > 10 or (c != 'P' and c != 'I'):
        print('Ocorreu um erro.')
        win = -1
    elif n <= 10 and c == 'P' or 'I':
        ia = random.randint(0, 10)
        s = ia + n
        if s % 2 == 0 and c == 'P':
            print(f'Você escolheu {n} e o computador {ia}. No total deu {n+ia} e esse é um número PAR. Parabéns, você ganhou!')
            count += 1
            win = True
        elif s % 2 != 0 and c == 'I':
            print(f'Você escolheu {n} e o computador {ia}. No total deu {n + ia} e esse é um número ÍMPAR. Parabéns, você ganhou!')
            count += 1
            win = True
        elif s % 2 != 0 and c == 'P':
            print(f'Você escolheu {n} e o computador {ia}. No total deu {n + ia} e esse é um número ÍMPAR. Infelizmente você perdeu!')
            win = False
        elif s % 2 == 0 and c == 'I':
            print(f'Você escolheu {n} e o computador {ia}. No total deu {n + ia} e esse é um número PAR. Infelizmente você perdeu!')
            win = False
    if not win:
        if count > 1:
            print(f'PARABÉNS! Você ganhou {count} vezes.')
            count = 0
        elif count == 1:
            print(f'PARABÉNS! Você ganhou {count} vez.')
            count = 0
        else:
            print(f'Infelizmente você não ganhou nenhuma vez!')
        end = str(input('Digite S para CONTINUAR ou qualquer outra letra para ENCERRAR: ')).strip().upper()
        if end == 'S':
            print('=' * 30)
        else:
            break
print('Jogo ENCERRADO. Até mais.')







