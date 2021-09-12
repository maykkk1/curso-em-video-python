dados = dict()
jogador = str(input('Nome do jogador: '))
qntd_partidas = int(input(f'Quantas partidas {jogador} jogou: '))
gols_lista = list()
gc = 0
for x in range(0, qntd_partidas):
    gols = int(input(f'Gols marcados no {x + 1}º jogo: '))
    gc += gols
    gols_lista.append(gols)
dados['nome'] = jogador
dados['gols'] = gols_lista
dados['total'] = gc
print('=-' * 30)
print(dados)
print('=-' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador} jogou {qntd_partidas} partidas. ')
for pos, elemento in enumerate(gols_lista):
    print('{:>32}'.format(f'Na {pos + 1}º partida marcou {elemento} gols.'))
print(f'Marcou um total de {gc} gols.')




