import math
n = float (input('\033[:1:31mDigite um número decimal\033[m '))
print ('\033[:1:97mO valor digitado foi\033[m \033[:4:34m{}\033[m \033[:1:97me a sua porção inteira é\033[m \033[:4:34m{}\033[m '.format(n,math.trunc(n)))
