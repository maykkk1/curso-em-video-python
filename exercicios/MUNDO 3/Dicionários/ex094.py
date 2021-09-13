import pandas as pd
dados = list()
pessoa = dict()
mulheres = list()
acima_da_media = list()
tot = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [F/M]: ')).upper()
        if pessoa['sexo'] == 'F' or pessoa['sexo'] == 'M':
            break
        else:
            print('ERRO! Digite F para feminino ou M para masculino.')
    pessoa['idade'] = int(input('Idade: '))
    dados.append(pessoa.copy())
    end = ' '
    while end not in 'SN':
        end = str(input('Deseja continuar? [S/N]')).upper()
        if end == 'N' or end == 'S':
            break
        print('ERRO! Digite S para continuar ou N para encerrar.')
    if end == 'N':
        break
qntd_pessoas = len(dados)
for elemento in dados:
    tot += elemento['idade']
media = tot / qntd_pessoas
for elemento in dados:
    if elemento['sexo'] == 'F':
        mulheres.append(elemento.copy())
    if elemento['idade'] >= media:
        acima_da_media.append(elemento.copy())

print(f'A) Ao todo temos {qntd_pessoas} pessoas cadastradas. ')
print(f'B) A média de idade é de {media:.2f}')
print(f'C) As mulheres cadastradas foram', end=' ')
for v in mulheres:
    print(v['nome'], end=' ')
print('')
print(f'D) As pessoas com idade acima da média: ')
for elemento in acima_da_media:
    for k, v in elemento.items():
        print(f'{k} = {v};', end=' ')
    print('')
df = pd.DataFrame(dados)
print(df)