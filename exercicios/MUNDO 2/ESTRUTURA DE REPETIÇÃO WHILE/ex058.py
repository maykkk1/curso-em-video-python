import  random
print('Sou o seu computador, acabei de pensar em um número de 0 a 10 e dúvido que você adivinhe!')
n = random.randint(0, 10)
count_p = 1
print(n)
c = int(input('Digite seu palpite: '))
while c != n:
    if n > c:
        print('Maior... Tente novamente.')
    if n < c:
        print('Menor... Tente novamente.')
    c = int(input('Digite seu palpite: '))
    count_p += 1
print(f'Parabéns, você acertou! Precisou de {count_p} palpite(s).')