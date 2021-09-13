s = float(input('\033[:1:97mQual o salário do funcionário?\033[m \033[32mR$\033[m'))
a = s*0.15
print('\033[37mO funcionário que ganhava\033[m \033[31mR${}\033[m\033[37m, com o reajuste de\033[m \033[31m15%\033[m\033[37m, irá ganhar\033[m \033[31mR${:.2f}\033[m'.format(s,s+a))