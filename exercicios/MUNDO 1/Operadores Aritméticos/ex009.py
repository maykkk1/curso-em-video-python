n = int(input('Digite um número '))
t = 1
while(t <= 10):
    print('\033[37m{}\033[m \033[30mx\033[m \033[37m{}\033[m \033[30m=\033[m \033[37m{}\033[m'.format(n,t,n*t))
    t = t + 1