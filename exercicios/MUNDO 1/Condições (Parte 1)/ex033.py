v1 = int(input('Digite o primeiro número '))
v2 = int(input('Digite o segundo número  '))
v3 = int(input('Digite o terceiro número '))
maior = ()
menor = ()
if v1 > v2 and v1 > v3:
    maior = v1
    menor = v2 if v2 < v3 else v3
if v2 > v3 and v2 > v1:
    maior = v2
    menor = v1 if v1 < v2 else v2
if v3 > v1 and v3 > v2:
    maior = v3
    menor = v1 if v1 < v2 else v2
print(f'O maior número é {maior} e o menor número é {menor}')