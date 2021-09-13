import random
lista = ['Tesoura', 'Pedra', 'Papel']
print('Vamos jogar Jokenpô!')
print('Qual vai ser a sua jogada?')
print('[1]Pedra\n[2]Tesoura\n[3]Papel')
co = ()
while co != True:
    ia = random.randint(0, 2)
    iac = lista[ia]
    p = int(input('Digite a sua escolha: '))
    c = lista[p]
    if c == 'Tesoura' and iac == 'Tesoura':
        print(f'Você escolheu o {c} e o computador {iac}')
        print('Houve um empate, escolha novamente.')
    elif c == 'Pedra' and iac == 'Pedra':
        print(f'Você escolheu o {c} e o computador {iac}')
        print('Houve um empate, escolha novamente.')
    elif c == 'Papel' and iac == 'Papel':
        print(f'Você escolheu o {c} e o computador {iac}')
        print('Houve um empate, escolha novamente')
    elif c == 'Pedra' and iac == 'Tesoura':
        print(f'Você escolheu o {c} e o computador {iac}')
        print('Parabens, você ganhou!')
        co = True
    elif c == 'Papel' and iac == 'Pedra':
        print(f'Você escolheu o {c} e o computador {iac}')
        print('Parabéns, você ganhou!')
        co = True
    elif c == 'Tesoura' and iac == 'Papel':
        print(f'Você escolheu o {c} e o computador {iac}')
        print('Parabéns, você ganhou!')
        co = True
    elif c == 'Tesoura' and iac == 'Pedra':
        print(f'Você escolheu o {c} e o computador {iac}')
        print('Você perdeu!')
        co = True
    elif c == 'Papel' and iac == 'Tesoura':
        print(f'Você escolheu o {c} e o computador {iac}')
        print('Você perdeu!')
        co = True
    elif c == 'Pedra' and iac == 'Papel':
        print(f'Você escolheu o {c} e o computador {iac}')
        print('Você perdeu!')
        co = True


