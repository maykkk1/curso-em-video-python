c = [
     '\033[;30;107m',  # 0 - Branco
     '\033[;30;102m',  # 1 - Verde
     '\033[;30;41m',   # 2 - Vermelho
     '\033[;30;44m'    # 3 - Azul
    ]


def title(msg, color=0):
    size = len(msg) + 4
    print(f'{c[color]}~' * size)
    print(' ', msg)
    print('~' * size)


def pyHelp(string):
    title(f'Analisando a documentação de {string}', color=3)
    print('\033[;30;107m')
    help(string)


#programa principal
while True:
    title('SISTEMA DE AJUDA PyHELP', color=1)
    function_lib = str(input('\033[mFunção ou Biblioteca: ')).lower()
    if function_lib.upper() == 'FIM':
        break
    pyHelp(function_lib)


title('Até logo!', color=2)
