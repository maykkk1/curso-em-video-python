def title(txt, c=0):
    print(f'{color(c)}-'*44)
    print(txt.center(44))
    print('-'*44)


def color(c=0):
    color_list = [
                  '\033[m',    # 0 - Sem cor
                  '\033[31m',  # 1 - Vermelho
                  '\033[32m',  # 2 - Verde
                  '\033[33m',  # 3 - Amarelo
                  '\033[34m',  # 4 - Azul
                  '\033[35m',  # 5 - Roxo
                 ]
    return color_list[c]


def menu_(list):
    title('MENU PRINCIPAL', 0)
    for element in list:
        for k, v in element.items():
            print(f'{color(3)}{k} - {color(4)}{v}')
    print(f'{color(0)}-' * 44)


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print(f'\033[31mErro! Por favor digite um número inteiro válido.\033[m')
            continue
        else:
            return num