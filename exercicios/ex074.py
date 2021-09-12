from random import randint

x = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
maior = 0
menor = 0
for pos, y in enumerate(x):
    if pos == 0:
        menor = y
        maior = y
    if y > maior:
        maior = y
    if y < menor:
        menor = y
print(x)
print(f'O maior número é {maior} e o menor é {menor}')


