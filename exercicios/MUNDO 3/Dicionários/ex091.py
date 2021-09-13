import operator
from operator import itemgetter
from random import randint
from time import sleep

jogadores = [{'name':'jogador1'}, {'name':'jogador2'}, {'name':'jogador3'}, {'name':'jogador4'}]
count = 1

jogadores[0]['dado'] = randint(1, 6)
jogadores[1]['dado'] = randint(1, 6)
jogadores[2]['dado'] = randint(1, 6)
jogadores[3]['dado'] = randint(1, 6)

for elemento in jogadores:
    for pos, item in enumerate(elemento.values()):
        if pos == 0:
            print(f'O {item} tirou', end=' ')
        else:
            print(f'{item} no dado.')
    sleep(0.8)
print('\n', '{:^29}'.format('RANKING DE JOGADORES'), '\n')
print('-='*15)
jogadores.sort(key=itemgetter('dado'), reverse=True)
for elemento in jogadores:
    for pos, v in enumerate(elemento.values()):
        if pos == 0:
            print(f'{count}º lugar: {v} com', end=' ')
        else:
            print(f'{v}.')
    count +=1
    sleep(0.8)