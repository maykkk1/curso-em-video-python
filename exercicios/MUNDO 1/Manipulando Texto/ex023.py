num = str(input('\033[;1;97mDigite um numero '))
while len(num) == 1:
    print('Analisando o numero \033[;1;91m{}'.format(num))
    print('\033[;1;97mUnidade:\033[;1;91m{}\033[;1;97m\nDezena:\033[;1;91m{}\033[;1;97m\nCentena:\033[;1;91m{}\033[;1;97m\nMilhar:\033[;1;91m{}'.format(num,0,0,0))
    break
while len(num) == 2:
    print('\033[;1;97mAnalisando o numero \033[;1;91m{}'.format(num))
    print('\033[;1;97mUnidade:\033[;1;91m{}\033[;1;97m\nDezena:\033[;1;91m{}\033[;1;97m\nCentena:\033[;1;91m{}\033[;1;97m\nMilhar:\033[;1;91m{}'.format(num[0],num[1],0,0))
    break
while len(num) == 3:
    print('\033[;1;97mAnalisando o numero \033[;1;91m{}'.format(num))
    print('\033[;1;97mUnidade:\033[;1;91m{}\033[;1;97m\nDezena:\033[;1;91m{}\033[;1;97m\nCentena:\033[;1;91m{}\033[;1;97m\nMilhar:\033[;1;91m{}'.format(num[2],num[1],num[0],0))
    break
while len(num) == 4:
    print('\033[;1;97mAnalisando o numero \033[;1;91m{}'.format(num))
    print('\033[;1;97mUnidade:\033[;1;91m{}\033[;1;97m\nDezena:\033[;1;91m{}\033[;1;97m\nCentena:\033[;1;91m{}\033[;1;97m\nMilhar:\033[;1;91m{}'.format(num[3],num[2],num[1],num[0]))
    break
while len(num) > 4:
    print('\033[;1;91mDigite no máximo 4 digitos')
    break