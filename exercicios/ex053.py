f = str(input('Digite uma frase: ')).replace(' ', '',).lower()
f = f.replace('ô','o')
f = f.replace('ó','o')
f = f.replace(',','')
f = f.replace('-','')
f = f.replace('í','i')
f = f.replace('á','a')
f = f.replace('â','a')
f = f.replace('ã','a')
f = f.replace('.','')
y = []
for item in reversed(f):
    y.append(item)
y = ''.join(y)
if f == y:
    print(f'O inverso de {f} é {y}.\nTemos um PALÍDROMO')
else:
    print(f'O  inverso de {f} é {y}.\nNão é um PALÍDROMO')

