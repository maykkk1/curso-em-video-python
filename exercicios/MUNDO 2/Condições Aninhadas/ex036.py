c = float(input('Qual o valor da casa '))
s = float(input('Qual o valor do seu salário '))
a = int(input('Em quantos anos você pretende pagar? '))
vp = c / (a*12)
p = s * 0.30
if p < vp:
    print('Seu empréstimo foi \033[;1;91mNEGADO\033[m')
else:
    print('Seu empréstimo foi \033[;1;92mACEITO\033[m')