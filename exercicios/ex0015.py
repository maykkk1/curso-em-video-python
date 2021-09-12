d = int (input('\033[:1:97mQuantos dias alugados?\033[m '))
k = float (input('\033[:1:97mQuanto km você rodou?\033[m ' ))
print ('\033[:1:97mO total a pagar é \033[m\033[:4:31mR${:.2f}\033[m'.format((60*d)+(0.15*k)))