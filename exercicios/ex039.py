import datetime
ano_atual = datetime.date.today().year
data = int(input('Qual é o ano do seu nascimento? '))
idade = ano_atual - data
print(f'Quem nasceu em {data} faz {idade} anos em {ano_atual}.')
if data >= ano_atual:
    print(f'Então você é um viajante do futuro? ')
elif idade < 18:
    d = 18 - idade
    print(f'Ainda faltam {d} ano(os) para o seu alistamento.')
    print(f'Você deverá se alistar no ano de {ano_atual + d}')
elif idade == 18:
    print(f'Você deve se alistar \033[;1;91mIMEDIATAMENTE\033[m.')
else:
    d = idade - 18
    print(f'Seu ano de alistamento foi {ano_atual-d}. Você está atrasado há {d} ano(os).')
