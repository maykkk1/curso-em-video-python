from numeros import moeda, aumentar, diminuir, double, half
price = float(input('Digite o preço: '))

print(f'A metade de {moeda(price)} é {half(price, True)}')
print(f'O dobro de {moeda(price)} é {double(price, True)}')
print(f'Aumentando 10% de {moeda(price)}, temos {aumentar(price, 10, True)}')