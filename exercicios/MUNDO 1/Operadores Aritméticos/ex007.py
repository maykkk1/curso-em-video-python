n1 = float(input('Digte a primeira nota do aluno '))
n2 = float(input('Digite a segundo nota do aluno '))
n3 = float(input('Digite a terceira nota do aluno '))
n4 = float(input('Digite a quarta nota do aluno '))

m = ((n1 + n2 + n3 + n4)/4)

print ('A média final do aluno foi \33[1:40:31m{:.2f}\33[m.'.format(m))
