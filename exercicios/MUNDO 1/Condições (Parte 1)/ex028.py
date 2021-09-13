import random
from time import sleep

n = random.randint(1, 5)
a = int(input('Digite um numero de 1 a 5: '))
print('processando ')
sleep(1)
print('Você acertou' if a == n else 'Você perdeu')

print(a, n)
