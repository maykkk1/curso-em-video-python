import numeros
price = float(input('Digite o preço: '))

print(f'A metade de {numeros.moeda(price)} é {numeros.moeda(numeros.half(price))}')
print(f'O dobro de {numeros.moeda(price)} é {numeros.moeda(numeros.double(price))}')
print(f'Aumentando 10% de {numeros.moeda(price)}, temos {numeros.moeda(numeros.aumentar(price, 10))}')