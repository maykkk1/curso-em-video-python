import datetime
ano_atual = datetime.datetime.today().year
pessoas = []
count = 0
while count < 7:
    pessoas.append(int(input('Digite o ano do seu nascimento: ')))
    count += 1
maior = 0
menor = 0
for x in pessoas:
    if ano_atual - x >= 18:
        maior += 1
    elif ano_atual - x < 18:
        menor += 1
print(f'{maior} pessoas já atingiram a maioridade e {menor} ainda não.')