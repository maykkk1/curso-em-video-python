#================= Sequência de Fibonacci ======================

count = int(input('Digite quantos termos de Fibonacci você quer ver: '))
n1 = 0
n2 = 1
while count >= 1:
    if n1 == 0:
        print(n1, end=' ➝ ')
        print(n2, end=' ➝ ')
        count -= 2
    soma = n1 + n2
    n1 = n2
    n2 = soma
    count -= 1
    if count == 0:
        print(soma, end=' FIM!')
    else:
        print(soma, end=' ➝ ')
