l1 = float(input('Digite o valor do primeiro lado '))
l2 = float(input('Digite o valor do segundo lado '))
l3 = float(input('Digite o valor do terceiro lado '))
if l1 + l2 > l3 and l3 + l1 > l2 and l2 + l3 > l1:
    if l1 == l2 and l2 == l3:
        print(f'Esse é um triângulo Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print(f'Esse é um triângulo Isóceles ')
    else:
        print(f'Esse é um triângulo Escaleno')
else:
    print(f'Os segmentos acima NÃO podem formar um triângulo!')