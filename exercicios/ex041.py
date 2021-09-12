import datetime
ano_atual = datetime.date.today().year
nasc = int(input('Digite o ano do seu nascimento '))
idade = ano_atual - nasc
if idade < 3:
    print(f'Idade incompatível')
elif idade <= 9:
    print(f'O atleta tem {idade} anos.\nClassificação: MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos.\nClassificação: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos.\nClassificação: JUNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos.\nClassificação: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos.\nClassificação: MASTER')