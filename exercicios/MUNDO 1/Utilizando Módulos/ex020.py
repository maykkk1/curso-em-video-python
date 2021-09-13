import random
nomes = ['','','','']
qntNomes = 1
pos = 0
while qntNomes < 5:
    nomes[pos] = str(input('\033[;1;36mDigite o nome do aluno\033[m '))
    qntNomes = qntNomes + 1
    pos = pos + 1
random.shuffle(nomes)
print('\033[;1;97mO primeiro aluno a se apresentar será\033[m \033[3;37m{}\033[m\033[;1;97m, o segundo será\033[m \033[3;37m{}\033[m\033[;1;97m,'
      ' o terceiro será\033[m \033[3;37m{}\033[m \033[;1;97me o ultimo será\033[m \033[3;37m{}\033[m\033[;1;97m.'.format(nomes[0],nomes[1],nomes[2],nomes[3]))