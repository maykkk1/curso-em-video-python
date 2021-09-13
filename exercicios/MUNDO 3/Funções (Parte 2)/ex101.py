def voto(x):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - x
    if 18 <= idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade >= 16 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: NÃO VOTA'


nasc = int(input('Informe a data de nascimento: [xxxx] '))

print(voto(nasc))

