from datetime import datetime
cadastro = {}
ano_atual = datetime.now().year
while True:
    cadastro['nome'] = str(input('Nome: '))
    ano_nasc = int(input('Ano de nascimento: '))
    cadastro['idade'] = ano_atual - ano_nasc
    cadastro['sexo'] = str(input('Sexo: [M/F] ')).upper()
    CTPS = int(input('Carteira de trabalho [0 não ter]: '))
    if CTPS == 0:
        break
    else:
        cadastro['CTPS'] = CTPS
        ano_contratacao = int(input('Ano de Contratação: '))
        cadastro['Ano de Contratação'] = ano_contratacao
        cadastro['Salário'] = float(input('Salário: '))
        idade_contratado = ano_contratacao - ano_nasc
        if cadastro['sexo'] == 'M':
            cadastro['aposentadoria'] = idade_contratado + 35
            break
        else:
            cadastro['aposentadoria'] = idade_contratado + 30
            break
for k, v in cadastro.items():
    print(f'- {k} tem o valor {v}.')