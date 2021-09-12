x = int(input('Digite um número '))
d = (x*2)
t = (x*3)
r = (x**(1/2))
cores = {'red':'\33[1:31m','limpa':'\33[m'}

print('O dobro desse número é {}{}{}\nO triplo é {}{}{}\nA raiz é {}'
      '{:.0f}{}'.format(cores['red'],d,cores['limpa'],cores['red'],t,cores['limpa'],cores['red'],r,cores['limpa']))
