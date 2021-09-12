from random import sample
from time import sleep

primaryList = list()
secundaryList = list()

qnt = int(input('Quantos jogos deseja criar? '))

for element in range(0, qnt):
    secundaryList = sample(range(1, 60), 6)
    secundaryList.sort()
    primaryList.append(secundaryList[:])
    secundaryList.clear()

for pos, jogo in enumerate(primaryList):
    print(f'Jogo {pos + 1}: {jogo}')
    sleep(0.6)