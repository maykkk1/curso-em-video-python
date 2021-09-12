count_m = 0
media = 0
gender = ()
oldAge = 0
oldMan = ()
checkM = False
for p in range(1,5):
    print('-'*5,f'{p}º Pessoa','-'*5)
    name = str(input('Digite o nome: ')).strip()
    age = int(input('Digite a idade: '))
    media += age
    while gender != 'M' and gender != 'F':
        gender = str(input('Digite seu gênero sexual [M/F] ')).upper()
    if age < 20 and gender == 'F':
        count_m +=1
    if gender == 'M':
        if age > oldAge:
            oldMan = name
            oldAge = age
            checkM = True
    gender = ()

print(f'A média de idade é {media/4}.')
if checkM == True:
    print(f'O homem mais velho se chama {oldMan} e tem {oldAge} anos.\n')
if count_m > 1:
    print(f'Ao todo há {count_m} mulheres com menos de 20 anos')
elif count_m == 1:
    print(f'Há apenas uma mulher com menos de 20 anos.')
else:
    print('Não há mulheres com menos de 20 anos.')
