v = float(input('Digite o valor do seu salário R$:'))
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(v,(v*0.15)+v)if v <= 1250.00 else
      'Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(v,(v*0.10)+v))