import pandas as pd
time = list()
layout = ['cod','nome', 'gols', 'total']
jogador = dict()
gols = list()
cont = 0
cod = 0
while True:
    jogador['cod'] = cod
    jogador['nome'] = str(input('Nome: ')).upper()
    qnt_partidas = int(input('Quantidade de partidas jogadas: '))
    for partida in range(0, qnt_partidas):
        gols.append(int(input(f'Quantidade de gols marcados na {partida + 1}º partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    end = ' '
    while end not in 'SN':
        end = str(input('Deseja continuar? ')).upper()[0]
        if end == 'S' or end == 'N':
            break
        else:
            print('ERRO! Digite S para continuar ou N para parar.')
    cod += 1
    if end == 'N':
        break

print('-=' * 30)

for pos, elemento in enumerate(layout):
    if pos == 0:
        print('{:<4}'.format(elemento), end=' ')
    elif pos == 1:
        print('{:<15}'.format(elemento), end=' ')
    elif pos == 2:
        print('{:<10}'.format(elemento), end=' ')
    else:
        print('{:<5}'.format(elemento), end=' ')
print('')
print('-' * 39)
for elemento in time:
    for pos, jogador in enumerate(elemento.values()):
        if pos == 0:
            print('{:<4}'.format(f'{jogador}'), end=' ')
        elif pos == 1:
            print('{:<15}'.format(f'{jogador}'), end=' ')
        elif pos == 2:
            print('{:<15}'.format(f'{jogador}'), end=' ')
        else:
            print('{:<5}'.format(f'{jogador}'), end=' ')
    print('')

while True:
    while True:
        jogador_dados = int(input('Digite o index do jogador que queira ver o desempenho individual: [999 para parar]: '))
        if jogador_dados == 999:
            break
        elif 0 <= jogador_dados <= len(time) - 1:
            print(f'-- LEVANTAMENTO DO JOGADOR {time[jogador_dados]["nome"]}')
            for pos, gols in enumerate(time[jogador_dados]['gols']):
                print(f'Na {pos + 1}º partida o jogador marcou {gols} gols.  ')

        else:
            print('Não há jogador com o index informado.')
    if jogador_dados == 999:
        break
print('>>>Finalizando<<<')