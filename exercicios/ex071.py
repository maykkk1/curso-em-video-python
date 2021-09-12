print('='*30)
print('{: ^30}'.format('BANCO BTC'))
print('='*30)
nota1 = nota10 = nota20 = nota50 = 0
dinheiro = float(input('Quanto deseja sacar? '))
while dinheiro > 0:
    if dinheiro > 50:
        nota50 = int(dinheiro) // 50
        dinheiro -= (nota50*50)
        print(f'Total de {nota50} cédula(s) de R$50')
    if dinheiro > 20:
        nota20 = int(dinheiro) // 20
        dinheiro -= (nota20*20)
        print(f'Total de {nota20} cédula(s) de R$20')
    if dinheiro > 10:
        nota10 = int(dinheiro) // 10
        dinheiro -= (nota10*10)
        print(f'Total de {nota10} cédula(s) de R$10')
    if dinheiro > 1:
        nota1 = int(dinheiro) // 1
        dinheiro -= (nota1*1)
        print(f'Total de {nota1} cédula(s) de R$1')

print('FIM!')





