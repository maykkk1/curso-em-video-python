p = float(input('\033[:1:97mQual o preço do produto?\033[m '))
d = p*0.05
print('\033[:1:37mO produto que custava\033[m \033[31mR${}\033[m\033[:1:37m, com\033[m \033[31m5%\033[m \033[:1:37mde desconto custará\033[m \033[31mR${:.2f}\033[m.'.format(p,p-d))