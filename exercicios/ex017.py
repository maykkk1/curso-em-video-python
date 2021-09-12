from math import hypot
o = float(input('Qual o comprimento do cateto oposto? '))
a = float(input('Qual o comprimento do cateto adjacente? '))
r = (o**2)+(a**2)
print('O valor da hipotenusa é {:.2f}.'.format(hypot(o, a)))
