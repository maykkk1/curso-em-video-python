def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except KeyboardInterrupt:
            print('\n\033[;31mO usuário preferiu não digitar um número.\033[m')
            num = 0
            return num
        except:
            print('\033[;31mErro! Por favor digite um número inteiro válido.\033[m')


def leiaFloat(msg):
    num = str(input(msg)).replace(',', '.')
    try:
        num = float(num)
        return num
    except KeyboardInterrupt:
        print('\n\033[;31mO usuário preferiu não digitar um número.\033[m')
        num = 0
        return num
    except:
        print('\033[;31mErro! Por favor digite um número real válido.\033[m')


real = leiaFloat('Digite um número real: ')
inteiro = leiaInt('Digite um número inteiro: ')

print(f'Numero real = {real}\n'
      f'Numero inteiro = {inteiro}')