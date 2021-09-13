name = str(input('Digite seu nome completo ')).strip().lower()
print('Seu primeiro nome é {}'.format(name.capitalize().split()[0]))
print('Seu ultimo nome é {}'.format(name.title().split()[-1]))