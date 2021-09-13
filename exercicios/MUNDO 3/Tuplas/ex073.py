times = ('Palmeiras', 'Atlético-MG', 'Forteleza', 'Bragantino', 'Athletico-PR',
         'Ceará', 'Fluminense', 'Bahia', 'Flamengo', 'Santos',
         'Atlético-GO', 'Corinthians', 'Juventude', 'São Paulo', 'Internacional',
         'América-MG', 'Sport', 'Cuiabá', 'Grêmio', 'Chapecoense')

print(f'Os 4 primeiros colocados são {times[:4]}')
print(f'Os 4 últimos colocados são {times[16:]}')
print(sorted(times))
for pos, x in enumerate(times):
    if x == 'Chapecoense':
        print(f'O {x} está na {pos+1}º posição.')