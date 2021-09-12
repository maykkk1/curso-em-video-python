import random
nomes =  ['','','','']
qtdNomes = 1
pos = 0
while qtdNomes < 5:
    nomes[pos] = str(input('\033[:1:97mDigite um nome\033[m '))
    qtdNomes = qtdNomes + 1
    pos = pos + 1
print('\033[;1;97mA pessoa sorteada foi o(a)\033[m \033[4;31m{}\033[m\033[;1;97m.\033[m'.format(random.choice(nomes)))