print('='*30)
print('\033[:1:91m      LOJA SUPER BARATÃO\033[m')
print('='*30)
sum = 0
count = 0
baratoName = ' '
baratoPreco = 0
first = True
while True:
    name = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    sum += preco
    if preco >= 1000:
        count += 1
    if first == True or preco < baratoPreco:
        baratoName = name
        baratoPreco = preco
        first = False
    end = ' '
    while end not in 'SN':
        end = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if end == 'N':
        break
print(f'O total da compra foi de R${sum:.2f}')
print(f'O total de produtos que custam mais de R$1000.00 é: {count}')
print(f'O produto mais barato foi: {baratoName} Custo: R${baratoPreco} ')

