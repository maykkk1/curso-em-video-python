while True:
    n = int(input('Deseja saber a tabuada de qual número? '))
    if n >= 0:
        for x in range(1,11):
            print(f'{x} x {n} = {x*n}')
    if n < 0:
        print('Programa de tabuada ENCERRADO! Volte sempre.')
        break