def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print(f'\033[31mErro! Por favor digite um número inteiro válido.\033[m')
            continue
        else:
            return num