c = float(input('\033[:1:97mInforme a temperatura em ºC\033[m '))
f = (c*1.8)+32
print('\033[:1:37m{}ºC\033[m \033[:1:97mé equivalente a\033[m \033[37m{:.1f}°F\033[m'.format(c,f))