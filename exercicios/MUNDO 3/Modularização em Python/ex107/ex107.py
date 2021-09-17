import numeros
price = float(input('Digite o preço: '))

print(f'A metade de {price} é {numeros.half(price)}')
print(f'O dobro de {price} é {numeros.double(price)}')
print(f'Aumentando 10% de {price}, temos {numeros.aumentar(price, 10)}')
